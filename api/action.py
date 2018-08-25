# -*- coding: utf-8 -*-

class Action:
	def __init__(self, klass, handler):
		self._class = klass
		self._handler = handler

	def __before():
		if getattr(self._class, 'before'):
			self._class.before()

	def __after(result):
		if getattr(self._class, 'after'):
			return self._class.after(result)
		else:
			return result

	def execute(self, *args):
		self.__before(*args)
		result = self._handler(*args)
		return self.__after(result)
