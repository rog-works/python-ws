# -*- coding: utf-8 -*-

class Action:
	def __init__(self, obj, handler):
		self._obj = obj
		self._handler = handler

	@property
	def name(self) -> str:
		return self._handler.__name__

	def __before(self):
		if hasattr(self._obj, 'before'):
			self._obj.before()

	def __after(self, response):
		if hasattr(self._obj, 'after'):
			return self._obj.after(response)
		else:
			return response

	def initialize(self, *args):
		if hasattr(self._obj, 'initialize'):
			self._obj.initialize(*args)

	def execute(self):
		self.__before()
		response = self._handler()
		return self.__after(response)
