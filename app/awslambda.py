# -*- coding: utf-8 -*-

from app.bootstrap import Bootstrap
from data.config import Config
from di.di import register
from router.router import Router
from net.request import Request, Builder
from error.errors import Error

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

	def run(self, config: Config, event: dict) -> dict:
		"""イベントデータから対応するハンドラーを呼び出し、レスポンスを返却

		Args:
			event: イベントデータ

		Returns:
			レスポンスの連想配列
		"""
		try:
			request = self.__build_request(event)
			Bootstrap(config, request)
			router = Router(config.get('routes.path'))
			receiver = router.dispatch(request.url)
			handler = receiver.instantiate(config, request)
			return handler().to_dict()
		except Error as e:
			raise Exception(f'{e.code}: message = {e.message}')
