# -*- coding: utf-8 -*-

import unittest
from tests.helper.fixture import data_provider
from router.router import Router

class TestRouter(unittest.TestCase):
	def test_dispatch(self):
		router = Router('tests/fixtures/router/router/routes.yml')
		class_type, method_name = router.dispatch('/test/Router')
		self.assertEqual('TestRouter', class_type.__name__)
		self.assertEqual('handle', method_name)
