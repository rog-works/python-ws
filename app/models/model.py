# -*- coding: utf-8 -*-

import json

class Model(object):
	@classmethod
	def api(cls, api: str, data: dict = {}) -> dict:
		return {
			'key': 'hoge',
			'value': {
				'id': 1,
				'type': 2,
				'v': 3,
				'valts': 4,
				'val': 5,
			}
		}
		#with Api().post(api, data) as res:
		#	try:
		#		return json(res)
		#	except ValueError as e:
		#		raise DataFormatError(f'JSON decode error. message = {e}')

	def to_dict(self):
		assert False, f'Not implemented to_dict.'
