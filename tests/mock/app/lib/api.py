# -*- config: utf-8 -*-

import os
import md5
import yaml

class MockApi(object):
	def post(self, path: str, params: dict, auth: dict) -> dict:
		fixtures = self.__load_fixtures(path)
		digest = self.__digest(params, auth)
		return fixtures[digest]

	def __digest(self, *args: tuple) -> str:
		return md5.new(*args).hexdigest()

	def __load_fixtures(self, path: str, digest: str) -> dict:
		filepath = f'{os.getcwd()}/tests/mock/app/lib/fixtures/{path}.yml'
		with open(filepath) as f:
			fixtures = {}
			for values in yaml.load(f).values():
				digest = self.__digest(*values['args'])
				fixtures[digest] = values['data']
			return fixtures

