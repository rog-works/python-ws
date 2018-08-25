# -*- coding: utf-8 -*-

import os
import yaml

class Router:
	def __init__(self):
		self._routes = self.__load()

	def __load(self):
		path = os.path.join(os.getcwd(), 'config', 'routes.yml')
		if os.path.exists():
			raise ''

		f = open(path)
		data = yaml.load(f)
		f.close()
		return data

	def resolve(self, path: str):
		 if not path in self._routes:
			 raise 'Undefined route. path = {}'.format(path)

		 return self._routes[path]
