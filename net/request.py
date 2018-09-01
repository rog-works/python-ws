# -*- coding: utf-8 -*-

import copy

class Request(object):
	"""リクエスト情報の管理"""

	def __init__(self, url: str, method: str, headers: dict, queries: dict, body: dict):
		"""インスタンスを生成

		:param str url: URL
		:param str method: メソッド
		:param str headers: ヘッダー
		:param str queries: クエリー
		:param str body: リクエストボディ
		"""
		self._url = url
		self._method = method
		self._headers = headers
		self._queries = queries
		self._body = body

	@property
	def url(self) -> str:
		"""URLを取得するプロパティ"""
		return self._url

	@property
	def method(self) -> str:
		"""メソッドを取得するプロパティ"""
		return self._method

	def has_header(self, key: str) -> bool:
		"""指定のヘッダーが存在するか判定

		:return bool: True = 存在
		"""
		return key in self._headers

	def header(self, key: str, default = None) -> str:
		"""指定のヘッダー値を取得。キーが存在しない場合はデフォルト値を返却

		:param str key: ヘッダーキー
		:param any default: デフォルト値
		:return str: ヘッダー値
		"""
		return self._headers[key] if key in self._headers else default

	def has_query(self, key: str) -> bool:
		"""指定のクエリーが存在するか判定

		:return bool: True = 存在
		"""
		return key in self._queries

	def query(self, key: str, default = None) -> str:
		"""指定のクエリー値を取得。キーが存在しない場合はデフォルト値を返却

		:param str key: クエリーキー
		:param any default: デフォルト値
		:return str: クエリー値
		"""
		return self._queries[key] if key in self._queries else default

	@property
	def queries(self) -> dict:
		"""クエリーを取得するプロパティ"""
		return copy.deepcopy(self._queries)

	@property
	def body(self) -> dict:
		"""リクエストボディを取得するプロパティ"""
		return copy.deepcopy(self._body)

class Builder(object):
	"""リクエストの生成情報の管理とリクエストの生成"""

	def __init__(self):
		"""インスタンスを生成"""
		self._url = ''
		self._method = ''
		self._headers = {}
		self._queries = {}
		self._body = {}

	def url(self, url: str):
		"""URLを設定

		:param str url: URL
		"""
		self._url = url

	def method(self, method: str):
		"""メソッドを設定

		:param str method: メソッド
		"""
		self._method = method

	def headers(self, headers: dict):
		"""ヘッダーを設定

		:param dict headers: ヘッダー
		"""
		self._headers = headers

	def add_header(self, key: str, value: str):
		"""ヘッダーを追加

		:param str key: ヘッダーキー
		:param str value: 値
		"""
		self._headers[key] = value

	def queries(self, queries: dict):
		"""クエリーを設定

		:param dict queries: クエリー
		"""
		self._queries = queries

	def add_query(self, key: str, value: str):
		"""クエリーを追加

		:param str key: クエリーキー
		:param str value: 値
		"""
		self._queries[key] = value

	def body(self, body: dict):
		"""リクエストボディを設定

		:param dict body: リクエストボディ
		"""
		self._body = body

	def build(self) -> Request:
		"""リクエストを生成

		:return Request: リクエスト
		"""
		return Request(self._url, self._method, self._headers, self._queries, self._body)
