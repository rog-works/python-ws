# -*- config: utf-8 -*-

from enum import IntEnum

class LogLevels(IntEnum):
	DEBUG = 1
	INFO = 2
	WARNING = 3
	ERROR = 4
	CRITICAL = 5

class Logger(object):
	def __init__(self, level = LogLevels.DEBUG):
		self._allow_level = level if type(level) is not str else LogLevels[level]

	def level(self, level: LogLevels):
		self._allow_level = level

	def _can_write(self, write_level: LogLevels):
		return self._allow_level <= write_level

	def debug(self, *args):
		assert True, f'Not implemented {self.__name__}'

	def info(self, *args):
		assert True, f'Not implemented {self.__name__}'

	def warning(self, *args):
		assert True, f'Not implemented {self.__name__}'

	def error(self, *args):
		assert True, f'Not implemented {self.__name__}'

	def critical(self, *args):
		assert True, f'Not implemented {self.__name__}'
