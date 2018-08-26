# -*- coding: utf-8 -*-

from app.controllers.controller import Controller

class TestApp(Controller):
	def handle(self):
		return self.view({})
