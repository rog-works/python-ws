# -*- coding: utf-8 -*-

from net.response import Response
from app.controllers.controller import Controller

class GetDevice(Controller):
	"""デバイス情報取得コントローラー"""

	def before(self):
		"""アクションの事前処理"""
		print(f'invoked #before via = {self.action.name}')

	def after(self, response: Response) -> Response:
		"""アクションの事後処理

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
		return self.view({'scceed': True})
