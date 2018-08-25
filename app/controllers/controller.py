# -*- coding: utf-8 -*-

from api.action import Action
from api.request import Request
from api.response import Response

class Controller(object):
	"""コントローラーの基底クラス。コントローラー共通の処理を定義

	Attributes:
		_action: アクション
		_request: リクエスト
	"""

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
		"""アクションを取得するプロパティ

		Returns:
			アクション
		"""
		return self._action

	@property
	def request(self) -> Request:
		"""リクエストを取得するプロパティ

		Returns:
			リクエスト
		"""
		return self._request

	def json(self, data: dict) -> Response:
		"""JSONのレスポンスを生成

		Args:
			data: レスポンスデータ

		Returns:
			レスポンス
		"""
		return Response(data)
