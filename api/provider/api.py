# -*- config: utf-8 -*-

import json
from data.config import Config
from di.container import Container as DI

class Api(object):
    @property
    def user() -> dict:
        return DI.instance.get('api.user')

    @property
    def config() -> Config:
        return DI.instance.get('config')

    def GetDevice(self, primary_id) -> dict:
        return self.post('/api/GetDevice', {'id': primary_id})

    def GetAllDevices(self) -> dict:
        return self.post('/api/GetAllDevices')

    def SetDevice(self, data: dict):
        return self.post('/api/SetDevice', data)

    def post(self, api: str, data: dict = {}) -> dict:
        headers = {
            'Content-Type': 'application/json'
        }
        body = {
            'user_id': self.user.id,
            'user_token': self.user.token,
            'access_key': self.config.get('api.access_key'),
            'access_token': self.config.get('api.access_token'),
            'req_id': random.nextint(1, 10000),
            'signature': md5(12345).digest()
        }
        url = f'{self.config.get("api.host")}{api}'
        with urlopen(url, header=headers, body=body) as res:
            data = json.loads(res)
            return Mapper.changed_by(data)

