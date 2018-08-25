# -*- coding: utf-8 -*-

class Request:
	def __init__(self, url: str, headers: dict, query: dict, body: dict):
		self._url = url
		self._headers = headers
		self._query = query
		self._body = body

	@property
	def url() -> str:
		return self._url

	def headers(self, key: str, default = None):
		return self._headers[key] if key in self._headers else default

	def query(self, key: str, default = None):
		return self._query[key] if key in self._query else default

	def body(self) -> dict:
		return self._body

class Builder:
	def __init__(self):
		self._url = ''
		self._headers = {}
		self._query = {}
		self._body = {}

	def url(self, url: str) -> Builder:
		self._url = url
		return self

	def headers(self, headers: dict) -> Builder:
		self._headers = headers

	def add_header(self, key: str, value) -> Builder:
		self._headers[key] = value
		return self

	def query(self, query: dict) -> Builder:
		self._query = query

	def add_query(self, key: str, value) -> Builder:
		self._query[key] = value
		return self

	def body(self, body: dict) -> Builder:
		self._body = body
		return self

	def build() -> Request:
		return Request(self._url, self._headers, self._query, self._body)
