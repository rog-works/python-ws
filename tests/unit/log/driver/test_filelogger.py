# -*- coding: utf-8 -*-

import os
import unittest
from log.logger import LogLevels
from log.driver.filelogger import FileLogger
from tests.helper.fixture import data_provider

class TestRequest(unittest.TestCase):
	@data_provider(lambda : [
		(r'\d{4}(-\d{2}){2} (:?\d{2}){3} \[DEBUG\] hoge', LogLevels.DEBUG.name, 'hoge'),
		(r'\d{4}(-\d{2}){2} (:?\d{2}){3} \[INFO\] 1234', LogLevels.INFO.name, 1234),
		(r'\d{4}(-\d{2}){2} (:?\d{2}){3} \[WARNING\] \[1234\]', LogLevels.WARNING.name, [1234]),
		(r'\d{4}(-\d{2}){2} (:?\d{2}){3} \[ERROR\] {\'hoge\': 1234}', LogLevels.ERROR.name, {'hoge': 1234}),
		(r'\d{4}(-\d{2}){2} (:?\d{2}){3} \[CRITICAL\] True', LogLevels.CRITICAL.name, True),
	])
	def test_write(self, expected, level: str, message: str):
		method = level.lower()
		logger = self.__create(level)
		writer = getattr(logger, method)
		writer(message)
		self.assertRegex(self.__latest_line(), expected)

	@data_provider(lambda : [
		(5, LogLevels.DEBUG.name),
		(4, LogLevels.INFO.name),
		(3, LogLevels.WARNING.name),
		(2, LogLevels.ERROR.name),
		(1, LogLevels.CRITICAL.name),
	])
	def test_level(self, expected: int, level: str):
		self.__remove_log_file()
		logger = self.__create(level)
		logger.debug('debug')
		logger.info('info')
		logger.warning('warning')
		logger.error('error')
		logger.critical('critical')
		self.assertEqual(expected, self.__line_count())

	def __create(self, level: str) -> FileLogger:
		return FileLogger(level, 'logs/test_app.log')

	def __remove_log_file(self):
		log_path = self.__log_path()
		if os.path.exists(log_path):
			os.remove(log_path)

	def __log_path(self) -> str:
		return f'{os.getcwd()}/logs/test_app.log'

	def __latest_line(self) -> str:
		log_path = self.__log_path()
		with open(log_path, mode='r', encoding='utf-8') as f:
			return f.read().split('\n')[-2]

	def __line_count(self) -> int:
		log_path = self.__log_path()
		with open(log_path, mode='r', encoding='utf-8') as f:
			return len(f.read().split('\n')) - 1
