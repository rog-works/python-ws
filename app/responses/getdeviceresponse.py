# -*- coding: utf-8 -*-

from net.response import Response
from app.models.device import Device

class GetDeviceResponse(Response):
	def __init__(self, device: dict, light_colors: list):
		self._device = device
		self._light_colors = light_colors

	def to_dict(self):
		data = {
			'key': self._device['key'],
			'value': {
				'id': self._device['id'],
				'type': self._device['type'],
				'v': self._device['v'],
				'valts': self._device['valts'],
				'val': self._device['val']
			}
		}

		if self._light_colors:
			data['light_colors'] = self._light_colors

		return data
