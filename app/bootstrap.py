# -*- config: utf-8 -*-

from importlib import import_module
from data.config import Config
from net.request import Request
from di.di import register

class Bootstrap(object):
	"""起動時の処理をまとめる"""

	def __init__(self, config: Config, request: Request):
		"""インスタンスを生成

		:param Config config: コンフィグ
		:param Request request: リクエスト
		"""
		self.__di_register(config, request)

	def __di_register(self, config: Config, request: Request):
		"""DIコンテナーへの登録

		:param Config config: コンフィグ
		:param Request request: リクエスト
		:raise DataFormatError: コンフィグ内のDI定義が不正
		"""
		self.__register_config(config)
		self.__register_request(request)

		deffinitions = config.get('di')
		if deffinitions:
			for key, deffinition in deffinitions.items():
				self.__register_by_deffinition(key, deffinition)

	def __register_by_deffinition(self, key: str, deffinition: dict):
		"""モジュール定義からDIコンテナーにモジュールファクトリーを登録

		:param str key: 登録キー
		:param dict deffinition: モジュール定義
		"""
		try:
			path = deffinition['path']
			module = deffinition['module']
			args = tuple(deffinition['args'])
			self.__register_di(key, path, module, *args)
		except ImportError as e:
			raise DataFormatError(f'Unexpected di deffinition. key = {key}, deffinition = {deffinition}')
		except AttributeError as e:
			raise DataFormatError(f'Unexpected di deffinition. key = {key}, deffinition = {deffinition}')

	@register('config')
	def __register_config(self, config: Config):
		"""モジュールファクトリーの生成(コンフィグ)

		:param Config config: コンフィグ
		:return function: モジュールファクトリー
		"""
		return lambda : config

	@register('request')
	def __register_request(self, request: Request):
		"""モジュールファクトリーの生成(リクエスト)

		:param Request request: リクエスト
		:return function: モジュールファクトリー
		"""
		return lambda : request

	@register()
	def __register_di(self, key: str, path: str, module: str, *args):
		"""モジュールファクトリーの生成

		:param str path: モジュールパス
		:param str module: モジュール名
		:param tuple *args: モジュールへの引数
		:return tuple: 登録キーとモジュールファクトリーのタプル
		"""
		return key, lambda : getattr(import_module(path), module)(*args)
