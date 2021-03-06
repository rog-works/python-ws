# -*- coding: utf-8 -*-

class Error(Exception):
	"""例外の基底クラス。エラーメッセージとエラーコードを管理"""

	def __init__(self, message: str, code: int):
		"""インスタンスを生成

		:param str message: エラーメッセージ
		:param int code: エラーコード
		"""
		self._message = message
		self._code = code

	@property
	def message(self) -> str:
		"""エラーメッセージを取得するプロパティ"""
		return self._message

	@property
	def code(self) -> int:
		"""エラーコードを取得するプロパティ"""
		return self._code

class IllegalArgumentError(Error):
	"""引数などの入力値が不正である事を示す"""
	def __init__(self, message: str):
		super().__init__(message, 400)

class IndexOutOfBoundError(Error):
	"""配列の境界外のインデックスを指定した事を示す"""
	def __init__(self, message: str):
		super().__init__(message, 400)

class DataFormatError(Error):
	"""ファイルなどのデータ形式が不正である事を示す"""
	def __init__(self, message: str):
		super().__init__(message, 400)

class UnauthorizedError(Error):
	"""認証に失敗した事を示す"""
	def __init__(self, message: str):
		super().__init__(message, 401)

class NotPermittedError(Error):
	"""実行権限がない事を示す"""
	def __init__(self, message: str):
		super().__init__(message, 403)

class NotFoundError(Error):
	"""ファイルやデータが存在しない事を示す"""
	def __init__(self, message: str):
		super().__init__(message, 404)

class RouteMissmatchError(Error):
	"""未定義のルートを指定した事を示す"""
	def __init__(self, message: str):
		super().__init__(message, 404)
