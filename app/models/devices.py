# -*- coding: utf-8 -*-

from app.models.model import Model

class Devices(Model):
	@classmethod
	def get(cls):
		return cls(cls.api('GetAllDevices'))
