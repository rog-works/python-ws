# -*- coding: utf-8 -*-

from api.request import Request
from api.response import Response
from app.controllers.controller import Controller

class GetDevice(Controller):
	"""デバイス情報取得コントローラー"""

	def before(self):
		"""ハンドラーの事前処理"""
		print(f'invoked #before via = {self.action.name}')

	def after(self, response: Response) -> Response:
		"""ハンドラーの事後処理

		Args:
			response: レスポンス

		Returns:
			レスポンス
		"""
		print('invoked #after')
		return response

	def show(self) -> Response:
		"""デバイス情報を取得

		Returns:
			レスポンス
		"""
		print('invoked #show')
		return self.json({'scceed': True})
