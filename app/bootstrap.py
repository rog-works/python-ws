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
		register('config', lambda : config)
		register('request', lambda : request)

		deffinitions = config.get('di')
		if deffinitions:
			try:
				for key, deffinition in deffinitions.items():
					path = deffinition['path']
					module = deffinition['module']
					args = tuple(deffinition['args'])
					register(key, self.__lazy_load_module(path, module, *args))
			except ImportError as e:
				raise DataFormatError(f'Unexpected di deffinition. key = {key}, deffinition = {deffinition}')
			except AttributeError as e:
				raise DataFormatError(f'Unexpected di deffinition. key = {key}, deffinition = {deffinition}')

	def __lazy_load_module(self, path: str, module: str, *args):
		"""モジュールファクトリーの生成

		:param str path: モジュールパス
		:param str module: モジュール名
		:param tuple *args: モジュールへの引数
		:return function: モジュールファクトリー
		"""
		return lambda : getattr(import_module(path), module)(*args)
