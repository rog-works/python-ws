# -*- coding: utf-8 -*-

from net.response import Response
from app.controllers.controller import Controller
from app.models.device import Device
from app.models.lightcolors import LightColors
from app.responses.getdeviceresponse import GetDeviceResponse

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
		device = Device.get(self.request.query('id'))
		light_colors = LightColors.get() if device.has_color else []
		return GetDeviceResponse(
			device.to_dict(),
			light_colors
		)
