# -*- config: utf-8 -*-

import os
from datetime import datetime
from log.logger import LogLevels, Logger
from error.errors import NotPermittedError

class FileLogger(Logger):
	"""ログマネージャ。出力したログをファイルに書き出す"""

	def __init__(self, level: str, path: str):
		"""インスタンスを生成

		:param str level: 出力レベル
		:param str path: ファイルの相対パス
		:raise NotPermittedError: ファイルの出力権限がない
		"""
		super().__init__(LogLevels[level])

		filepath = self.__file_path(path)
		if not os.access(os.path.dirname(filepath), os.W_OK):
			raise NotPermittedError(f'Cannot write. filepath = {filepath}')

		self._filepath = filepath

	def __file_path(self, path: str) -> str:
		"""出力するファイルの絶対パスを取得

		:param str path: ファイルの相対パス
		:return str:
		"""
		return os.path.abspath(f'{os.getcwd()}/{path}')

	def debug(self, *args):
		"""ログ出力(DEBUG)

		:param tuple *args: 出力パラメータ
		"""
		self.__write_line(LogLevels.DEBUG, *args)

	def info(self, *args):
		"""ログ出力(INFO)

		:param tuple *args: 出力パラメータ
		"""
		self.__write_line(LogLevels.INFO, *args)

	def warning(self, *args):
		"""ログ出力(WARNING)

		:param tuple *args: 出力パラメータ
		"""
		self.__write_line(LogLevels.WARNING, *args)

	def error(self, *args):
		"""ログ出力(ERROR)

		:param tuple *args: 出力パラメータ
		"""
		self.__write_line(LogLevels.ERROR, *args)

	def critical(self, *args):
		"""ログ出力(CRITICAL)

		:param tuple *args: 出力パラメータ
		"""
		self.__write_line(LogLevels.CRITICAL, *args)

	def __write_line(self, write_level: LogLevels, *args):
		"""1行ログ出力

		:param LogLevels write_level: 出力レベル
		:param tuple *args: 出力パラメータ
		"""
		if self._can_write(write_level):
			values = [
				datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
				f'[{write_level.name}]'
			]
			values.extend(list(map(str, args)))
			self.__flush(' '.join(values))

	def __flush(self, line: str):
		"""ログ出力

		:param str line: 出力行
		"""
		with open(self._filepath, mode='a', encoding='utf-8') as f:
			f.write(f'{line}\n')
