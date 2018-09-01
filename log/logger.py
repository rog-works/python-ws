# -*- config: utf-8 -*-

from enum import IntEnum

class LogLevels(IntEnum):
	"""ログレベルを管理するEnum"""

	DEBUG = 1
	INFO = 2
	WARNING = 3
	ERROR = 4
	CRITICAL = 5

class Logger(object):
	"""ログマネージャの基底クラス。出力ログの扱いは派生クラスで実装する"""

	def __init__(self, level = LogLevels.DEBUG):
		"""インスタンスを生成"""
		self._allow_level = level if type(level) is not str else LogLevels[level]

	@property
	def level(self) -> LogLevels:
		"""ログの主力レベルを取得するプロパティ"""
		return self._allow_level

	def _can_write(self, write_level: LogLevels) -> bool:
		"""ログ出力可能な出力レベルか判定

		:param LogLevels write_level: 出力レベル
		:return bool:
		"""
		return self._allow_level <= write_level

	def debug(self, *args):
		"""ログ出力(DEBUG)

		:param tuple *args: 出力パラメータ
		"""
		assert False, f'Not implemented debug.'

	def info(self, *args):
		"""ログ出力(INFO)

		:param tuple *args: 出力パラメータ
		"""
		assert False, f'Not implemented info.'

	def warning(self, *args):
		"""ログ出力(WARNING)

		:param tuple *args: 出力パラメータ
		"""
		assert False, f'Not implemented warning.'

	def error(self, *args):
		"""ログ出力(ERROR)

		:param tuple *args: 出力パラメータ
		"""
		assert False, f'Not implemented error.'

	def critical(self, *args):
		"""ログ出力(CRITICAL)

		:param tuple *args: 出力パラメータ
		"""
		assert False, f'Not implemented critical.'
