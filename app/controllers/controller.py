# -*- coding: utf-8 -*-

from data.config import Config
from router.action import Action
from net.request import Request
from net.response import Response

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
