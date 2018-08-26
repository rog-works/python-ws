# -*- coding: utf-8 -*-

from router.router import Router
from router.action import Action
from net.request import Request, Builder
from errors.error import Error

class AwsLambda(object):
	"""AWS Lambda用アプリケーション"""

	def __build_request(self, event: dict) -> Request:
		"""イベントデータからリクエストを生成

		Args:
			event: イベントデータ

		Returns:
			リクエスト
		"""
		builder = Builder()
		if 'url' in event:
			builder.url(event['url'])
		if 'headers' in event:
			builder.headers(event['headers'])
		if 'queries' in event:
			builder.queries(event['queries'])
		if 'body' in event:
			builder.body(event['body'])
		return builder.build()

	def run(self, event: dict) -> dict:
		"""イベントデータから対応するハンドラーを呼び出し、レスポンスを返却

		Args:
			event: イベントデータ

		Returns:
			レスポンスの連想配列
		"""
		try:
			request = self.__build_request(event)
			action = Action(*Router().dispatch(request.url))
			action.initialize(action, request)
			return action.execute().to_dict()
		except Error as e:
			raise Exception(f'{e.code}: message = {e.message}')
