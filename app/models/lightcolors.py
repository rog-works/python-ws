# -*- coding: utf-8 -*-

class LightColors(object):
	@classmethod
	def get(cls):
		return cls()

	def to_dict(self):
		return {
			'items': [0x000000, 0xFFFFFF],
		}
