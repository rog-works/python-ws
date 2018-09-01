# -*- config: utf-8 -*-

import os
from datetime import datetime
from log.logger import LogLevels, Logger
from error.errors import IllegalArgumentError

class FileLogger(Logger):
	def __init__(self, level: str, path: str):
		super().__init__(LogLevels[level])

		filepath = self.__file_path(path)
		if not os.access(os.path.dirname(filepath), os.W_OK):
			raise IllegalArgumentError(f'Cannot write. filepath = {filepath}')

		self._filepath = filepath

	def __file_path(self, path: str) -> str:
		return os.path.abspath(f'{os.getcwd()}{path}')

	def debug(self, *args):
		self.__write_line(LogLevels.DEBUG, *args)

	def info(self, *args):
		self.__write_line(LogLevels.INFO, *args)

	def warning(self, *args):
		self.__write_line(LogLevels.WARNING, *args)

	def error(self, *args):
		self.__write_line(LogLevels.ERROR, *args)

	def critical(self, *args):
		self.__write_line(LogLevels.CRITICAL, *args)

	def __write_line(self, write_level: LogLevels, *args):
		if self._can_write(write_level):
			values = [
				datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
				f'[{write_level.name}]'
			]
			values.extend(list(map(str, args)))
			self.__flush(' '.join(values))

	def __flush(self, line: str):
		with open(self._filepath, mode='a', encoding='utf-8') as f:
			f.write(f'{line}\n')
