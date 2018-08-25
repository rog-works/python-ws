# -*- coding: utf-8 -*-

import os
import yaml
import importlib
import re

class Router:
	def __init__(self):
		self._routes = self.__load(self.__config_path())

	def __config_path(self) -> str:
		return os.path.join(os.getcwd(), 'config', 'routes.yml')

	def __load(self, path: str) -> dict:
		if not os.path.exists(path):
			raise RuntimeError(f'Not found route configuretion. path = "{path}"')

		f = open(path)
		data = yaml.load(f)
		f.close()
		return data

	def __resolveDeffinition(self, route: str) -> tuple:
		if not route in self._routes:
			raise RuntimeError(f'Undefined route. route = "{route}"')

		deffinition = self._routes[route]
		if not re.match(r'^[\w.]+#[\w]+\.[\w]+$', deffinition):
			raise RuntimeError(f'Unexpected route deffinition. deffinition = "{deffinition}"')

		module, handler = deffinition.split('#')
		klass, method = handler.split('.')
		return module, klass, method

	def __resolveHander(self, module: str, klass: str, method: str) -> tuple:
		try:
			mod = importlib.import_module(module)
			obj = getattr(mod, klass)()
			handler = getattr(obj, method)
			return obj, handler
		except Exception as e:
			raise RuntimeError(f'Undefined handler. hander = {klass}.{method}, error = {e}')

	def dispatch(self, route: str) -> tuple:
		deffinition = self.__resolveDeffinition(route)
		return self.__resolveHander(*deffinition)
