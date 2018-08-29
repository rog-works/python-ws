# -*- coding: utf-8 -*-

from data.config import Config
from di.di import inject
from net.request import Request
from net.response import Response

class Controller(object):
	"""コントローラーの基底クラス。コントローラー共通の処理を定義"""

	@inject('config', 'request')
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

	def before(self):
		print('called base before')

	def after(self, response: Response) -> Response:
		print('called base after')
		return response