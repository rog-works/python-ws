# -*- coding: utf-8 -*-

from error.errors import NotFoundError, IllegalArgumentError

class __Container(object):
	"""DIコンテナ。ファクトリーの登録とインスタンスの生成・取得"""

	__instance = None

	@classmethod
	def instance(cls):
		"""インスタンスを取得

		:return __Container:
		"""
		if not cls.__instance:
			cls.__instance = cls()
		return cls.__instance

	def __init__(self):
		"""インスタンスを生成"""
		self._factories = {}
		self._caches = {}

	def get(self, key: str):
		"""登録キーに対応するファクトリーからインスタンスを生成して返却

		:param: str key: 登録キー
		:return any: キーに対応するインスタンス
		"""
		if key not in self._factories:
			raise NotFoundError(f'Undefined key. key = "{key}"')

		if self._caches[key] is not None:
			return self._caches[key]

		self._caches[key] = self._factories[key]()
		return self._caches[key]

	def register(self, key: str, factory):
		"""ファクトリーを登録

		:param: str key: 登録キー
		:param: function factory: ファクトリー
		"""
		if not callable(factory):
			raise IllegalArgumentError(f'Unexpected factory. expected callable')

		self._factories[key] = factory
		self._caches[key] = None

def register(key: str, factory):
	"""ファクトリーをDIコンテナに登録

	:param: str key: 登録キー
	:param: function factory: ファクトリー
	"""
	__Container.instance().register(key, factory)

def inject(*keys):
	"""指定の関数にインスタンスを注入する関数デコレーター

	:example:
		@inject('register_key')
		def func(self, inject_instance):
			pass

	:param: tuple *key: 注入する登録キーリスト
	"""
	def decorator(wrapper_func):
		def wrapper(*args):
			di = __Container.instance()
			instances = list(map(di.get, keys))
			args_list = list(args)
			args_list.extend(instances)
			return wrapper_func(*tuple(args_list))
		return wrapper
	return decorator
