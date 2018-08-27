# -*- coding: utf-8 -*-

from app.models.model import Model

class Device(Model):
    @classmethod
    def create(cls, data):
        return cls.api().AddDevice(data)

    @classmethod
    def get(cls, id: str):
        return cls(cls.api().GetDevice())

    @classmethod
    def all(cls) -> list:
        return cls.api().GetAllDevices().map(lambda row: cls(row))

    @classmethod
    def update(cls, data: dict):
        cls.api().SetDevice(data)

    @classmethod
    def delete(cls, primary_id):
        cls.api().DeleteDevice(primary_id)

    def on(self):
        self.__class__.update(self.to_on_data())

    def off(self):
        self.__class__.update(self.to_off_data())

    def bright(self, power: int):
        self.__class__.update(self.to_bright_data())

    def volume(self, power: int):
        self.__class__.update(self.to_volume_data())

