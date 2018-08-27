# -*- coding: utf-8 -*-

import yaml
import re
from jsonschema import validate
import imoprtlib.machinery as imm

class Mapper:
	@classmethod
	def has(cls, api: str):
		return os.path.exists(cls.__mapper_path(api))

	@classmethod
	def __schema_path(cls, api: str):
		return f'{os.getcwd()}/mappings/{api}-schema.yml'

	@classmethod
	def __mapper_path(cls, api: str):
		return f'{os.getcwd()}/mappings/{api}.py'

	def __init__(api: str):
		self._api = api
		self._schema = self.__load_schema(self._api)
		self._mapper = self.__load_mapper(self._api)

	@property 
	def schema_from(self):
		return self._schema['from'] if 'from' in self._schema else None

	@property
	def schema_to(self):
		return self._schema['to'] if 'to' in self._schema else None

	def __load_schema(self, api: str):
		path = Mapper.__schema_path(api)
		if not os.path.exists(path):
			return {}

		f = open(path, 'r')
		data = yaml.load(f)
		f.close()
		return data

	def __load_mapper(self, api: str):
		path = self.__mapper_path(api)
		module_name = f'mappings.{api}'
		return imm.SourceFileLoader(module_name, path).load_module()

	def __validate(self, data: dict, schema: dict):
		if schema:
			validate(data, schema)

	def changed_by(self, data: dict):
		self.__validate(data, self.schema_from)
		changed = self._mapper.changed_by(data)
		self.__validate(changed, self.schema_to)
		return changed

