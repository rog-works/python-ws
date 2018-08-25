# -*- coding: utf-8 -*-

class Request:
	def __init__(self, url: str, headers: dict, queries: dict, body: dict):
		self._url = url
		self._headers = headers
		self._queries = queries
		self._body = body

	@property
	def url(self) -> str:
		return self._url

	def has_header(self, key: str) -> bool:
		return key in self._header

	def header(self, key: str, default = None):
		return self._headers[key] if key in self._headers else default

	def has_query(self, key: str) -> bool:
		return key in self._queries

	def query(self, key: str, default = None):
		return self._queries[key] if key in self._queries else default

	@property
	def body(self) -> dict:
		return self._body

class Builder:
	def __init__(self):
		self._url = ''
		self._headers = {}
		self._queries = {}
		self._body = {}

	def url(self, url: str):
		self._url = url
		return self

	def headers(self, headers: dict):
		self._headers = headers

	def add_header(self, key: str, value):
		self._headers[key] = value
		return self

	def queries(self, queries: dict):
		self._queries = queries

	def add_query(self, key: str, value):
		self._queries[key] = value
		return self

	def body(self, body: dict):
		self._body = body
		return self

	def build(self) -> Request:
		return Request(self._url, self._headers, self._queries, self._body)
