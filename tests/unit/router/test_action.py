# -*- coding: utf-8 -*-

import unittest
from router.action import Action
from tests.fixtures.router.action.fixture import Fixture

class TestAction(unittest.TestCase):
	def test_initialize(self, *args):
		obj, handler = Fixture().data_initialize()
		action = Action(obj, handler)
		action.initialize(1, 'hoge')
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
