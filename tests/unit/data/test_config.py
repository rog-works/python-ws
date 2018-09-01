# -*- coding: utf-8 -*-

import unittest
from data.config import Config

class TestConfig(unittest.TestCase):
	def test_get(self):
		config = Config('tests/unit/data/fixtures/config/config.yml')
		self.assertEqual(123, config.get('hoge.fuga.piyo'))
		self.assertEqual('value', config.get('arr.2.key'))
