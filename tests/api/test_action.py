# -*- coding: utf-8 -*-

import unittest
from api.action import Action

#def data_provider(data_provider_func):
#	def decorator(test_func):
#		def wrapper(self, *_):
#			for args in data_provider_func():
#				test_func(self, *args)
#		return wrapper
#	return decorator

class TestAction(unittest.TestCase):
	def test_initialize(self, *args):
		obj, handler = Fixture().data_initialize()
		action = Action(obj, handler)
		action.initialize(*(1, 'hoge'))
		self.assertEqual(1, obj.value)
		self.assertEqual('hoge', obj.string)

	def test_initialize_none(self):
		obj, handler = Fixture().data_initialize_none()
		action = Action(obj, handler)
		action.initialize(1, 'hoge')
		self.assertEqual(None, obj.value)
		self.assertEqual(None, obj.string)

	def test_execute(self):
		obj, handler = Fixture().data_execute()
		action = Action(obj, handler)
		self.assertEqual({'value': None, 'string': None}, action.execute())

	def test_execute_before(self):
		obj, handler = Fixture().data_execute_before()
		action = Action(obj, handler)
		self.assertEqual({'value': None, 'string': 'before'}, action.execute())

	def test_execute_after(self):
		obj, handler = Fixture().data_execute_after()
		action = Action(obj, handler)
		self.assertEqual({'value': 1, 'string': None}, action.execute())

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

if __name__ == '__main__':
	unittest.main()
