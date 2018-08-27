# -*- coding: utf-8 -*-

import json

class Model(object):
	@classmethod
	def api(cls, api: str, data: dict = {}) -> dict:
		with Api().post(api, data) as res:
			try:
				return json(res)
			except Exception as e:
				raise DataFormatError(f'JSON decode error. message = {e}')

	def to_dict(self):
		assert True, f'Not implemented method. {self.__class__.__name__}.{self.__name__}'
