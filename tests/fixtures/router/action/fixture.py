# -*- coding: utf-8 -*-

class Fixture(object):
	def data_initialize(self):
		class Handler(object):
			def __init__(self):
				self.value = None
				self.string = None

			def initialize(self, value: int, string: str):
				self.value = value
				self.string = string

			def handle(self):
				return {'value': self.value, 'string': self.string}

		obj = Handler()
		handler = getattr(obj, 'handle')
		return obj, handler

	def data_initialize_none(self):
		class Handler(object):
			def __init__(self):
				self.value = None
				self.string = None

			def handle(self):
				return {'value': self.value, 'string': self.string}

		obj = Handler()
		handler = getattr(obj, 'handle')
		return obj, handler

	def data_execute(self):
		class Handler(object):
			def __init__(self):
				self.value = None
				self.string = None

			def handle(self):
				return {'value': self.value, 'string': self.string}

		obj = Handler()
		handler = getattr(obj, 'handle')
		return obj, handler

	def data_execute_before(self):
		class Handler(object):
			def __init__(self):
				self.value = None
				self.string = None

			def before(self):
				self.string = 'before'

			def handle(self):
				return {'value': self.value, 'string': self.string}

		obj = Handler()
		handler = getattr(obj, 'handle')
		return obj, handler

	def data_execute_after(self):
		class Handler(object):
			def __init__(self):
				self.value = None
				self.string = None

			def after(self, res):
				res['value'] = 1
				return res

			def handle(self):
				return {'value': self.value, 'string': self.string}

		obj = Handler()
		handler = getattr(obj, 'handle')
		return obj, handler
