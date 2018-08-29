# -*- config: utf-8 -*-

import unittest
from di.di import register, inject

class TestContainer(unittest.TestCase):
	def test_register_and_inject(self):
		@inject('hoge')
		def injectx1_func(hoge):
			return hoge

		@inject('fuga')
		def injectx1_arg_func(arg, fuga):
			return arg, fuga

		@inject('fuga', 'piyo')
		def injectx2_arg_func(arg, fuga, piyo):
			return arg, fuga, piyo

		class InnerClass(object):
			@inject('hoge')
			def __init__(self, hoge):
				self.hoge = hoge

			@inject('fuga')
			def injectx1_arg_func(self, arg, fuga):
				return arg, fuga

			@inject('piyo')
			@classmethod
			def injectx1_argx2_func(cls, arg1, arg2, piyo):
				return arg1, arg2, piyo

		register('hoge', lambda : 123)
		register('fuga', lambda : '456')
		register('piyo', lambda : [789])

		self.assertEqual(123, injectx1_func())
		self.assertEqual(('arg1', '456'), injectx1_arg_func('arg1'))
		self.assertEqual(('arg1', '456', [789]), injectx2_arg_func('arg1'))
		self.assertEqual(123, InnerClass().hoge)
		self.assertEqual(('arg1', '456'), InnerClass().injectx1_arg_func('arg1'))
		with self.assertRaises(TypeError):
			InnerClass.injectx1_argx2_func('hoge', 'fuga')

