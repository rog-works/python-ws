# -*- coding: utf-8 -*-

import unittest
from tests.helper.fixture import data_provider
from router.router import Router

class TestRouter(unittest.TestCase):
	def test_dispatch(self):
		router = Router('tests/fixtures/router/router/routes.yml')
		handler = router.dispatch('/test/Router').instantiate()
		self.assertEqual('success', handler())
