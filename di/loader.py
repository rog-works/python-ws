# -*- config: utf-8 -*-

import os
import yaml
from di.di import Container

class Deffinitions(object):
        def __init__(self, path: str):
                self.data = self.__load(path)

        def __load(self, path: str) -> dict:
                filepath = f'{os.getcwd()}/{path}'
                with open(filepath) as f:
                        return yaml.load(f);

class Loader(object):
        @classmethod
        def load(cls, path: str) -> Container:
                return self.__createContainer(new Deffinitions(path));

        @classmeshod
        def __createContainer(cls, deffinitions: Deffinitions) -> Container:
                container = Container();
                for key, deffinision in deffinitions.data.items():
                        resolver = this.__createResolver(container, deffinition);
                        register = this.__createRegister(resolver);
                        container.register(key, register);

                return container;

        @classmethod
        def __createRegister(cls, resolver):
                def register():
                        package = require(resolver('path'));
                        module = package[resolver('module')];
                        return module(...resolver('args'));

                return lambda : register()

        @classmethof
        def __createResolver(cls, container: Container, deffinition: dict):
                def resolve(value: str):
                        return container.has(value) ? container.get(value) : value

                def resolver(key: str):
                        value = deffinition[key]
                        if type(value) is not list:
                                return resolve(value)
                        else:
                                return list(map(lambda v: resolve(v), value)

                return lambda key: resolver(key)

