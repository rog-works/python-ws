# -*- config: utf-8 -*-

import os
from importlib import import_module
from data.config import Config
from di.di import register

class Bootstrap(object):
	def __init__(self, config: Config):
		self.__di_register(config)

	def __di_register(self, config: Config):
		register('config', lambda : config)

		deffinitions = config.get('di')
		if deffinitions:
			try:
				for key, deffinition in deffinitions.items():
					module_path = deffinition['module']
					class_name = deffinition['class']
					args = tuple(deffinition['args'])
					register(key, lambda : getattr(import_module(module_path), class_name)(*args))
			except ImportError as e:
				raise DataFormatError(f'Unexpected di deffinition. key = {key}, deffinition = {deffinition}')
			except AttributeError as e:
				raise DataFormatError(f'Unexpected di deffinition. key = {key}, deffinition = {deffinition}')
