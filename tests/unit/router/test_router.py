# -*- coding: utf-8 -*-

import unittest
from tests.helper.fixture import data_provider
from router.router import Router

class TestRouter(unittest.TestCase):
	def test_dispatch(self):
		obj, handler = Router('tests/fixtures/router/router/routes.yml').dispatch('/test/Router')
		self.assertEqual('TestRouter', obj.__class__.__name__)
		self.assertEqual('handle', handler.__name__)
