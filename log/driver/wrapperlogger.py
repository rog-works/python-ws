# -*- config: utf-8 -*-

import logging
from log.logger import LogLevels, Logger

class WrapperLogger(Logger):
	"""ログマネージャ。python標準のログラッパー"""

	def __init__(self, level: str):
	"""インスタンスを生成"""
		super().__init__(LogLevels[level])
		self._logger = logging.getLogger()
		self._logger.setLevel(self.__to_logging_level(self._level))

	def __to_logging_level(self, level: LogLevels):
	"""python標準のログレベルに変換

	:params LogLevels level: ログレベル
	:return int:
	"""
		map = {
			LogLevels.DEBUG: logging.DEBUG,
			LogLevels.INFO: logging.INFO,
			LogLevels.WARNING: logging.WARNING,
			LogLevels.ERROR: logging.ERROR,
			LogLevels.CRITICAL: logging.CRITICAL,
		}
		return map[level]

	def debug(self, *args):
		"""ログ出力(DEBUG)

		:param tuple *args: 出力パラメータ
		"""
		self.__logger.debug(*args)

	def info(self, *args):
		"""ログ出力(INFO)

		:param tuple *args: 出力パラメータ
		"""
		self.__logger.info(*args)

	def warning(self, *args):
		"""ログ出力(WARNING)

		:param tuple *args: 出力パラメータ
		"""
		self.__logger.warning(*args)

	def error(self, *args):
		"""ログ出力(ERROR)

		:param tuple *args: 出力パラメータ
		"""
		self.__logger.error(*args)

	def critical(self, *args):
		"""ログ出力(CRITICAL)

		:param tuple *args: 出力パラメータ
		"""
		self.__logger.critical(*args)
