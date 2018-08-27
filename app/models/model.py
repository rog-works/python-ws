# -*- coding: utf-8 -*-

from di.container import Container as DI

class Model(object):
	@classmethod
	def create(cls, data: dict):
		return DI.instance.get('db').create(data)

	@classmethod
	def get(cls, primary_id):
		return cls(DI.instance.get('db').get(primary_id))

	@classmethod
	def find(cls, page: int = 1, limit: int = 10) -> list:
		for data in DI.instance.get('db').find(page, limit):
			rows.append(cls(data))
		return rows

	@classmethod
	def update(cls, data: dict):
		DI.instance.get('db').update(data)

	@classmethod
	def delete(cls, primary_id):
		DI.instance.get('db').delete(primary_id)

	@property
	def primary_id(self):
		assert True, 'Not implemented property.'

	def save(self):
		if not self.primary_id:
			self.primary_id = self.__class__.create(self.to_dict())
		else:
			self.__class__.update(self.to_dict())

	def remove(self):
		self.__class__.delete(self.primary_id)