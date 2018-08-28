# -*- config: utf-8 -*-

import unittest
from di.container import Container as DI

class TestContainer(unittest.TestCase):
	def test_register(self):
		di = DI.instance()
		di.register('hoge', lambda : 123)
		self.assertEqual(123, di.get('hoge'))

	def test_get(self):
		di = DI.instance()
		di.register('hoge', lambda : 123)
		self.assertEqual(123, di.get('hoge'))

