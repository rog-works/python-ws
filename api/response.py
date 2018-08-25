# -*- coding: utf-8 -*-

class Response:
	def __init__(self, data):
		self._data = data

	@property
	def content_type(self):
		return 'application/json'

	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, value):
		self._data = value

	def to_hash(self) -> dict:
		return self._data
