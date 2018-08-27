# -*- coding: utf-8 -*-

from typing import Callable

class Container(object):
	@classmethod
	def instance(cls):
		if not hasattr(cls, '__instance'):
			cls.__instance = cls()
		return cls.__instance

	def __init__(self):
		assert not hasattr(self.__class__, '__instance'), 'Do not call constructor directory'
		self._factories = {}
		self._instances = {}

	def get(self, key: str):
		if key not in self._factories:
			return None

		if key in self._instances:
			return self._instances[key]

		self._instances[key] = self._factories[key]()
		return self._instances[key]

	def register(self, key: str, factory: Callable[[], object]):
		self._factories[key] = factory
