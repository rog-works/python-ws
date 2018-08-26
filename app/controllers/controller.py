# -*- coding: utf-8 -*-

from api.action import Action
from api.request import Request
from api.response import Response

class Controller(object):
	"""コントローラーの基底クラス。コントローラー共通の処理を定義"""

	def __init__(self):
		"""インスタンスを生成"""
		self._action = None
		self._request = None

	def initialize(self, action: Action, request: Request):
		"""インスタンスの初期化処理

		Args:
			action: アクション
			request: リクエスト
		"""
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
