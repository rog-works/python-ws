# -*- coding: utf-8 -*-

class Response(object):
	"""レスポンスデータの基底クラス"""

	@property
	def raw(self):
		"""レスポンスデータの実体を取得"""
		pass

	def to_dict(self) -> dict:
		"""レスポンスデータを連想配列に変換"""
		pass
