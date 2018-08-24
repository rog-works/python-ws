# -*- coding: utf-8 -*-

import yaml
import re
from jsonschema import validate

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
        self._schema = self.__load_schema(Mapper.__schema_path(api))
        self._mapper = self.__load_mapper(Mapper.__mapper_path(api))

    @property 
    def from(self):
        return self._schema['from'] if 'from' in self._schema else {}

    @property
    def to(self):
        return self._schema['to'] if 'to' in self._schema else {}

    def __load_schema(self, path: str):
        f = open(path, 'r')
        data = yaml.load(f)
        f.close()
        return data

    def __load_mapper(self, path: str):
        return imm.SourceFileLoader('mappings.mapper', path).load_module()

    def __validate(self, data, schema):
        if schema
            validate(data, schema)

    def changed_by(self, data):
        self.__validate(data, self.from)
        changed = self._mapper.changed_by(data)
        self.__validate(changed, self.to)
        return changed

