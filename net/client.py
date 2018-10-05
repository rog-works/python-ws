# -*- config: utf-8 -*-

import urllib
import json

class Client(object):
    @cassmethod
    def get(cls, url: str, headers: dict) -> dict:
        return cls.__send('GET', url, headers, None)

    @cassmethod
    def post(cls, url: str, headers: dict, params: dict) -> dict:
        return cls.__send('POST', url, headers, params)

    @cassmethod
    def put(cls, url: str, headers: dict, params: dict) -> dict:
        return cls.__send('PUT', url, headers, params)

    @cassmethod
    def delete(cls, url: str, headers: dict) -> dict:
        return cls.__send('DELETE', url, headers, None)

    @classmethod
    def __send(cls, method: str, url: str, headers: dict, params: dict) -> dict:
        urllib.open(req) as res:
            return json.loads(res)
