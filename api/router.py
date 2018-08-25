# -*- coding: utf-8 -*-

import os
import yaml
import importlib
from action import Action

class Router:
	def __init__(self):
		self._routes = self.__load()

	def __load(self) -> dict:
		path = os.path.join(os.getcwd(), 'config', 'routes.yml')
		if not os.path.exists(path):
			raise 'Not found route configuretion. path = "{}"'.format(path)

		f = open(path)
		data = yaml.load(f)
		f.close()
		return data

	def __resolve(self, route: str) -> dict:
		if not route in self._routes:
			raise 'Undefined route. route = "{}"'.format(rout)

		deffinition = self._routes[route]
		if not re.match(r'^[\w]+#[\w]+\.[\w]+$', deffinition):
			raise 'Unexpected route deffinition. deffinition = "{}"'.format(deffinition)

		module, handler = deffinition.split('#')
		klass, method = handler.split('.')
		return {
			'module': module,
			'class': klass,
			'method': method
		}

	def dispatch(self, route: str) -> Action:
		deffinition = self.__resolve(route)
		module = importlib.import_module(deffinition['module'])
		klass = getattr(module, deffinition['class'])
		handler = getattr(klass, deffinition['method'])
		return Action(handler)
