# -*- config: utf-8 -*-

import logging
from log.logger import LogLevels, Logger

class WrapperLogger(Logger):
	def __init__(self, level: str):
		super().__init__(LogLevels[level])
		self._logger = logging.getLogger()
		self._logger.setLevel(self.__to_logging_level(self._level))

	def __to_logging_level(self, level: LogLevels):
		map = {
			LogLevels.DEBUG: logging.DEBUG,
			LogLevels.INFO: logging.INFO,
			LogLevels.WARNING: logging.WARNING,
			LogLevels.ERROR: logging.ERROR,
			LogLevels.CRITICAL: logging.CRITICAL,
		}
		return map[level]

	def debug(self, *args):
		self.__logger.debug(*args)

	def info(self, *args):
		self.__logger.info(*args)

	def warning(self, *args):
		self.__logger.warning(*args)

	def error(self, *args):
		self.__logger.error(*args)

	def critical(self, *args):
		self.__logger.critical(*args)
