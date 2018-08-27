# -*- coding: utf-8 -*-

from app.models.model import Model

class Device(Model):
	@classmethod
	def create(cls, data: dict):
		return cls.api('AddDevice', data)

	@classmethod
	def get(cls, id):
		return cls(cls.api('GetDevice', {'id': id}))

	@classmethod
	def update(cls, data: dict):
		cls.api('SetDevice', data)

	@classmethod
	def delete(cls, id):
		cls.api('DeleteDevice', {'id': id})

	def __init__(self, data: dict):
		self._key = data['key']
		self._id = data['value']['id']
		self._type = data['value']['type']
		self._v = data['value']['v']
		self._valts = data['value']['valts']
		self._val = data['value']['val']

	@property
	def has_color(self) -> bool:
		return False

	def on(self):
		self.__class__.update(self.to_on_data())

	def off(self):
		self.__class__.update(self.to_off_data())

	def brightness(self, power: int):
		self.__class__.update(self.to_brightness_data())

	def volume(self, power: int):
		self.__class__.update(self.to_volume_data())

	def to_dict(self) -> dict:
		return {
			'key': self._key,
			'id': self._id,
			'type': self._type,
			'v': self._v,
			'valts': self._valts,
			'val': self._val
		}
