# -*- coding: utf-8 -*-

import unittest
from data.config import Config
from app.lambdaapp import LambdaApp as App

class TestLambdaApp(unittest.TestCase):
	def test_run(self):
		config = Config('tests/unit/app/fixtures/lambdaapp/config.yml')
		response = App().run(config, {
			'url': '/test/App',
			'method': 'GET',
			'headers': {
				'Authorization': 'auth_key',
			},
			'queries': {
				'hoge': 'fuga',
			},
			'body': {
				'fizz': 'buzz',
			},
		})
		self.assertEqual({'success': True}, response)
