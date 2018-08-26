# -*- coding: utf-8 -*-

import unittest
from app.awslambda import AwsLambda as App

class TestAwsLambda(unittest.TestCase):
	def test_run(self):
		App().run({
			'url': '/api/GetDevice',
			'headers': {
				'Authorization': 'access_key'
			},
			'queries': {
				'hoge': 'fuga'
			},
			'body': {
				'fizz': 'buzz'
			}
		})
