# -*- coding: utf-8 -*-

class Fixture(object):
	def data_instantiate(self):
		class Handler(object):
			def __init__(self, value: int, string: str):
				self.value = value
				self.string = string

			def handle(self):
				return {'value': self.value, 'string': self.string}

		return Handler, 'handle'

	def data_execute(self):
		class Handler(object):
			def __init__(self):
				self.value = None
				self.string = None

			def handle(self):
				return {'value': self.value, 'string': self.string}

		return Handler, 'handle'
