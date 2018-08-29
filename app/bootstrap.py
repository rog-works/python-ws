# -*- config: utf-8 -*-

from importlib import load_module
from di.di import register
from data.config import Config

def Bootstrap(object):
	def __init__():
		di_register()

	def di_register(self):
		config = Config('config/app-dev.yml')
		register('config', lambda : config)
		for key, deffinition in config.get('di').items():
			module_path = deffinition['module']
			class_name = deffinition['class']
			args = tuple(deffinition['args'])
			register(key, lambda : getattr(load_module(module_path), class_name)(*args))
	
