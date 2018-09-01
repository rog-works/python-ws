# -*- coding: utf-8 -*-

import unittest
from data.config import Config
from app.lambdaapp import LambdaApp as App

class TestLambdaApp(unittest.TestCase):
	def test_run(self):
		config = Config('config/app-dev.yml')
		App().run(config, {
			'url': '/api/GetDevice',
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
