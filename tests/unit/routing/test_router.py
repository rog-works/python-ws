# -*- coding: utf-8 -*-

import unittest
from routing.router import Router

class TestRouter(unittest.TestCase):
	def test_dispatch(self):
		router = Router('tests/unit/routing/fixtures/router/routes.yml')
		handler = router.dispatch('/test/Router').instantiate()
		self.assertEqual('success', handler())
