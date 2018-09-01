# -*- coding: utf-8 -*-

from error.errors import NotFoundError, IllegalArgumentError

class __Container(object):
	__instance = None

	@classmethod
	def instance(cls):
		if not cls.__instance:
			cls.__instance = cls()
		return cls.__instance

	def __init__(self):
		self._factories = {}
		self._caches = {}

	def get(self, key: str):
		if key not in self._factories:
			raise NotFoundError(f'Undefined key. key = "{key}"')

		if key in self._caches:
			return self._caches[key]

		self._caches[key] = self._factories[key]()
		return self._caches[key]

	def register(self, key: str, factory):
		if not callable(factory):
			raise IllegalArgumentError(f'Unexpected factory. expected callable')

		self._factories[key] = factory

def register(key: str, factory):
	__Container.instance().register(key, factory)

def inject(*keys):
	def decorator(wrapper_func):
		def wrapper(*args):
			di = __Container.instance()
			key_list = list(map(lambda key: di.get(key), keys))
			args_list = list(args)
			args_list.extend(key_list)
			return wrapper_func(*tuple(args_list))
		return wrapper
	return decorator

