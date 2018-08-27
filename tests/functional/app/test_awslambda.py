# -*- coding: utf-8 -*-

import unittest
from data.config import Config
from app.awslambda import AwsLambda as App

class TestAwsLambda(unittest.TestCase):
	def test_run(self):
		config = Config('config/app-dev.yml')
		App().run(config, {
			'url': '/api/GetDevice',
			'headers': {
				'Authorization': 'auth_key'
			},
			'queries': {
				'hoge': 'fuga'
			},
			'body': {
				'fizz': 'buzz'
			}
		})
