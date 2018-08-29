# -*- config: utf-8 -*-

import unittest
from di.container import register, inject

class TestContainer(unittest.TestCase):
	def test_register_and_inject(self):
		register('hoge', lambda : 123)

		@inject('hoge')
		def inner_func(hoge):
			return hoge

		self.assertEqual(123, inner_func())

