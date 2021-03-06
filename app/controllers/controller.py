# -*- coding: utf-8 -*-

from data.config import Config
from net.request import Request
from net.response import Response
from log.logger import Logger
from di.di import inject

class Controller(object):
	"""コントローラーの基底クラス。コントローラー共通の処理を定義"""

	def __init__(self, config: Config, request: Request):
		"""インスタンスを生成"""
		self._config = config
		self._request = request

	@property
	def config(self) -> Config:
		"""コンフィグを取得するプロパティ"""
		return self._config

	@property
	def request(self) -> Request:
		"""リクエストを取得するプロパティ"""
		return self._request

	@property
	@inject('logger')
	def logger(self, logger: Logger) -> Logger:
		"""ログマネージャを取得するプロパティ"""
		return logger

	def before(self):
		"""ハンドラーの事前処理"""
		print('called base before')

	def after(self, response: Response) -> Response:
		"""ハンドラーの事後処理

		:param Response response: レスポンス
		:return Response: レスポンス
		"""
		print('called base after')
		return response