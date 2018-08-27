# -*- coding: utf-8 -*-

class Container(object):
	@classmethod
	def instance(cls):
		if not hasattr(cls, '__instance'):
			cls.__instance = cls()
		return cls.__instance

	def __init__(self):
		assert not hasattr(self.__class__, '__instance'), 'Do not call constructor directory'
		self._factories = {}
		self._caches = {}

	def get(self, key: str):
		if key not in self._factories:
			return None

		if key in self._caches:
			return self._caches[key]

		self._caches[key] = self._factories[key]()
		return self._caches[key]

	def register(self, key: str, factory):
		if not callable(factory):
			raise IllegalArgumentError(f'Unexpected factory. expected callable')

		self._factories[key] = factory
