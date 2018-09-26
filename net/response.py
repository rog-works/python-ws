# -*- coding: utf-8 -*-

class Response(object):
	"""レスポンスデータの基底クラス"""

	def to_dict(self) -> dict:
		"""レスポンスデータを連想配列に変換"""
		assert False, f'Not implemented to_dict.'
