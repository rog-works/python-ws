# -*- coding: utf-8 -*-

from app.config import Config
from router.router import Router
from router.action import Action
from net.request import Request, Builder
from errors.error import Error

class AwsLambda(object):
	"""AWS Lambda用アプリケーション"""

	def __init__(self, config: Config):
		self._config = config

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
			router = Router(self._config.get('routes.path'))
			action = Action(*router.dispatch(request.url))
			action.initialize(self._config, action, request)
			return action.execute().to_dict()
		except Error as e:
			raise Exception(f'{e.code}: message = {e.message}')
