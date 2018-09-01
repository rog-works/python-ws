# -*- coding: utf-8 -*-

import unittest
from net.request import Request, Builder
from tests.helper.fixture import data_provider

class TestRequest(unittest.TestCase):
	@data_provider(lambda: [
		('/path/to/hoge', ('/path/to/hoge', 'GET', {}, {}, {}))
	])
	def test_url(self, expected, args):
		self.assertEqual(expected, Request(*args).url)

	@data_provider(lambda: [
		(True, 'hoge', ('', 'GET', {'hoge': 1}, {}, {})),
		(False, 'fuga', ('', 'GET', {'hoge': 1}, {}, {}))
	])
	def test_has_header(self, expected, key, args):
		self.assertEqual(expected, Request(*args).has_header(key))

	@data_provider(lambda: [
		(1, 'hoge', ('', 'GET', {'hoge': 1}, {}, {})),
		(2, 'fuga', ('', 'GET', {'hoge': 1, 'fuga': 2}, {}, {}))
	])
	def test_header(self, expected, key, args):
		self.assertEqual(expected, Request(*args).header(key))

	@data_provider(lambda: [
		(True, 'hoge', ('', 'GET', {}, {'hoge': 1}, {})),
		(False, 'fuga', ('', 'GET', {}, {'hoge': 1}, {}))
	])
	def test_has_query(self, expected, key, args):
		self.assertEqual(expected, Request(*args).has_query(key))

	@data_provider(lambda: [
		(1, 'hoge', ('', 'GET', {}, {'hoge': 1}, {})),
		(2, 'fuga', ('', 'GET', {}, {'hoge': 1, 'fuga': 2}, {}))
	])
	def test_query(self, expected, key, args):
		self.assertEqual(expected, Request(*args).query(key))

	@data_provider(lambda: [
		({'hoge': 1}, ('', 'GET', {}, {}, {'hoge': 1})),
		({'hoge': 1, 'fuga': 2, 'piyo': 3}, ('', 'GET', {}, {}, {'hoge': 1, 'fuga': 2, 'piyo': 3}))
	])
	def test_body(self, expected, args):
		self.assertEqual(expected, Request(*args).body)

class TestBuilder(unittest.TestCase):
	def test_build(self):
		builder = Builder()
		builder.url('/path/to/hoge')
		builder.method('GET')
		builder.headers({'Authorization': 'auth_key'})
		builder.add_header('Content-Type', 'application/json')
		builder.queries({'page': 1})
		builder.add_query('limit', 10)
		builder.body({'content': 'hogefugapiyo'})
		req = builder.build()
		self.assertEqual('/path/to/hoge', req.url)
		self.assertEqual('GET', req.method)
		self.assertEqual('auth_key', req.header('Authorization'))
		self.assertEqual('application/json', req.header('Content-Type'))
		self.assertEqual(1, req.query('page'))
		self.assertEqual(10, req.query('limit'))
		self.assertEqual({'page': 1, 'limit': 10}, req.queries)
		self.assertEqual({'content': 'hogefugapiyo'}, req.body)
