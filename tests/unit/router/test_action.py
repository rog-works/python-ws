# -*- coding: utf-8 -*-

import unittest
from router.action import Action
from tests.fixtures.router.action.fixture import Fixture

class TestAction(unittest.TestCase):
	def test_instantiate(self, *args):
		klass, method_name = Fixture().data_instantiate()
		action = Action(klass, method_name)
		action.instantiate(1, 'hoge')
		self.assertEqual({'value': 1, 'string': 'hoge'}, action.execute())

	def test_execute(self):
		klass, method_name = Fixture().data_execute()
		action = Action(klass, method_name)
		self.assertEqual({'value': None, 'string': None}, action.execute())
