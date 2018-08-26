# -*- coding: utf-8 -*-

class Response(object):
	"""レスポンスデータを管理"""

	def __init__(self, data):
		"""インスタンスを生成

		Args:
			data: レスポンスデータ
		"""
		self._data = data

	@property
	def content_type(self) -> str:
		"""Content-Typeを取得するプロパティ"""
		return 'application/json'

	@property
	def data(self):
		"""レスポンスデータ取得プロパティ"""
		return self._data

	def to_dict(self) -> dict:
		"""レスポンスデータを連想配列に変換

		Returns
			レスポンスデータ
		"""
		return self._data
