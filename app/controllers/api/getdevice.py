# -*- coding: utf-8 -*-

from net.response import Response
from app.controllers.controller import Controller
from app.models.device import Device
from app.models.lightcolors import LightColors
from app.responses.getdeviceresponse import GetDeviceResponse
from app.plugins.behavior import behavior

class GetDevice(Controller):
	"""デバイス情報取得コントローラー"""

	def before(self):
		super().before()
		print('called sub before')

	def after(self, response: Response) -> Response:
		response = super().after(response)
		print('called sub after')
		return response

	@behavior(before, after)
	def handle(self) -> Response:
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
