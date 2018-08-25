# -*- coding: utf-8 -*-

from app.awslambda import AwsLambda as App

def test_app():
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

if __name__ == '__main__':
	test_app()