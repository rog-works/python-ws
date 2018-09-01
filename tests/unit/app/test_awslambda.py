# -*- coding: utf-8 -*-

import unittest
from data.config import Config
from app.awslambda import AwsLambda as App

class TestAwsLambda(unittest.TestCase):
	def test_run(self):
		config = Config('tests/fixtures/app/awslambda/config.yml')
		App().run(config, {
			'url': '/test/App',
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
