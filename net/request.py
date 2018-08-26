# -*- coding: utf-8 -*-

class Request(object):
	"""リクエスト情報の管理"""

	def __init__(self, url: str, headers: dict, queries: dict, body: dict):
		"""インスタンスを生成

		Args:
			url: URL
			headers: ヘッダー
			queries: クエリー
			body: リクエストボディ
		"""
		self._url = url
		self._headers = headers
		self._queries = queries
		self._body = body

	@property
	def url(self) -> str:
		"""URLを取得するプロパティ"""
		return self._url

	def has_header(self, key: str) -> bool:
		"""指定のヘッダーが存在するか判定

		Returns:
			True = 存在
		"""
		return key in self._headers

	def header(self, key: str, default = None):
		"""指定のヘッダー値を取得

		Args:
			key: クエリキー
			default: デフォルト値

		Returns:
			ヘッダー値
		"""
		return self._headers[key] if key in self._headers else default

	def has_query(self, key: str) -> bool:
		"""指定のクエリーが存在するか判定

		Returns:
			True = 存在
		"""
		return key in self._queries

	def query(self, key: str, default = None):
		"""指定のクエリー値を取得

		Args:
			key: クエリーキー
			default: デフォルト値

		Returns:
			クエリー値
		"""
		return self._queries[key] if key in self._queries else default

	@property
	def body(self) -> dict:
		"""リクエストボディを取得するプロパティ"""
		return self._body

class Builder(object):
	"""リクエストの生成情報の管理とリクエストの生成"""

	def __init__(self):
		"""インスタンスを生成"""
		self._url = ''
		self._headers = {}
		self._queries = {}
		self._body = {}

	def url(self, url: str):
		"""URLを設定

		Args:
			url: URL
		"""
		self._url = url

	def headers(self, headers: dict):
		"""ヘッダーを設定

		Args:
			headers: ヘッダー
		"""
		self._headers = headers

	def add_header(self, key: str, value):
		"""ヘッダーを追加

		Args:
			key: ヘッダーキー
			value: 値
		"""
		self._headers[key] = value

	def queries(self, queries: dict):
		"""クエリーを設定

		Args:
			queries: クエリー
		"""
		self._queries = queries

	def add_query(self, key: str, value):
		"""クエリーを追加

		Args:
			key: クエリキー
			value: 値
		"""
		self._queries[key] = value

	def body(self, body: dict):
		"""リクエストボディを設定

		Args:
			body: リクエストボディ
		"""
		self._body = body

	def build(self) -> Request:
		"""リクエストを生成

		Returns:
			リクエスト
		"""
		return Request(self._url, self._headers, self._queries, self._body)
