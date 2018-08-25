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
        return '{}/mappings/{}-schema.yml'.format(os.path.abspath(os.path.dirname(__file__)), api)

    @classmethod
    def __mapper_path(cls, api: str):
        return '{}/mappings/{}.py'.format(os.path.abspath(os.path.dirname(__file__)), api)

    def __init__(api: str):
        self._api = api
        self._schema = self.__load_schema(self._api)
        self._mapper = self.__load_mapper(self._api)

    @property 
    def schema_from(self):
        return self._schema['from'] if 'from' in self._schema else {}

    @property
    def schema_to(self):
        return self._schema['to'] if 'to' in self._schema else {}

    def __load_schema(self, api: str):
        path = Mapper.__schema_path(api)
        if not os.path.exists(path):
            return {}

        f = open(path, 'r')
        data = yaml.load(f)
        f.close()
        return data

    def __load_mapper(self, api: str):
        module_name = 'mappings.{}'.format(api)
        return imm.SourceFileLoader(module_name, path).load_module()

    def __validate(self, data: dict, schema: dict):
        if not schema == {}:
            validate(data, schema)

    def changed_by(self, data: dict):
        self.__validate(data, self.schema_from)
        changed = self._mapper.changed_by(data)
        self.__validate(changed, self.schema_to)
        return changed

