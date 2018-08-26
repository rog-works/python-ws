# -*- coding: utf-8 -*-

from data.config import Config
from router.action import Action
from net.request import Request
from net.response import Response

class Controller(object):
	"""コントローラーの基底クラス。コントローラー共通の処理を定義"""

	def __init__(self):
		"""インスタンスを生成"""
		self._config = None
		self._action = None
		self._request = None

	def initialize(self, config: Config, action: Action, request: Request):
		"""インスタンスの初期化処理

		Args:
			config: コンフィグ
			action: アクション
			request: リクエスト
		"""
		self._config = config
		self._action = action
		self._request = request

	@property
	def action(self) -> Action:
		"""アクションを取得するプロパティ"""
		return self._action

	@property
	def request(self) -> Request:
		"""リクエストを取得するプロパティ"""
		return self._request

	def view(self, data: dict) -> Response:
		"""レスポンスを生成

		Args:
			data: レスポンスデータ

		Returns:
			レスポンス
		"""
		return Response(data)
