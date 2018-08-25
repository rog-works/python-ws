# -*- coding: utf-8 -*-

class Response(object):
	"""レスポンスデータを管理

	Attributes:
		_data: レスポンスデータ
	"""

	def __init__(self, data):
		"""インスタンスを生成

		Args:
			data: レスポンスデータ
		"""
		self._data = data

	@property
	def content_type(self) -> str:
		"""Content-Typeを取得

		Returns:
			Content-Type
		"""
		return 'application/json'

	@property
	def data(self):
		"""レスポンスデータ取得プロパティ

		Returns:
			レスポンスデータ
		"""
		return self._data

	@data.setter
	def data(self, data):
		"""レスポンスデータ設定プロパティ

		Args:
			data: レスポンスデータ
		"""
		self._data = data

	def to_hash(self) -> dict:
		"""レスポンスデータを連想配列に変換

		Returns
			レスポンスデータ
		"""
		return self._data
