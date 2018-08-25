# -*- coding: utf-8 -*-

from application import Application

def test_application():
	Application().run({
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
	test_application()