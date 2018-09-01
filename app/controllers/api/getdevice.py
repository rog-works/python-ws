# -*- coding: utf-8 -*-

from net.response import Response
from di.di import inject
from app.libs.auth import authorize
from app.controllers.controller import Controller
from app.models.device import Device
from app.models.lightcolors import LightColors
from app.responses.getdeviceresponse import GetDeviceResponse
from app.plugins.behavior import behavior

class GetDevice(Controller):
	"""デバイス情報取得コントローラー"""

	@inject('authorize')
	def before(self, auth: dict):
		"""ハンドラーの事前処理"""
		super().before()
		print('called sub before')

	def after(self, response: Response) -> Response:
		"""ハンドラーの事後処理

		:param Response response: レスポンス
		:return Response: レスポンス
		"""
		response = super().after(response)
		print('called sub after')
		return response

	@behavior(before, after)
	def handle(self) -> Response:
		"""デバイス情報を取得

		:return Response: レスポンス
		"""
		self.logger.info('hogehoge', 12345, [12345], {'hoge': 'fuga'})
		device = Device.get(self.request.query('id'))
		light_colors = LightColors.get() if device.has_color else []
		return GetDeviceResponse(
			device.to_dict(),
			light_colors
		)
