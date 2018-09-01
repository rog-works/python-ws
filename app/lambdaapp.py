# -*- coding: utf-8 -*-

from app.bootstrap import Bootstrap
from data.config import Config
from routing.router import Router
from net.request import Request, Builder
from error.errors import Error

class LambdaApp(object):
	"""AWS Lambda用アプリケーション"""

	def __build_request(self, event: dict) -> Request:
		"""イベントデータからリクエストを生成

		:param dict event: イベントデータ
		:return Request: リクエスト
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

		:param Config config: コンフィグ
		:param dict event: イベントデータ
		:return dict: レスポンスの連想配列
		:raise Error: Error系の例外発生時にメッセージを整形して再出力
		"""
		try:
			request = self.__build_request(event)
			Bootstrap(config, request)
			router = Router(config.get('routes.path'))
			receiver = router.dispatch(request.url)
			handler = receiver.instantiate(config, request)
			return handler().to_dict()
		except Error as e:
			raise Exception(f'{e.code}: error = {type(e)}, message = {e.message}')
