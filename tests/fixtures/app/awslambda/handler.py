# -*- coding: utf-8 -*-

from net.response import Response
from app.controllers.controller import Controller

class TestApp(Controller):
	def handle(self):
		return DummyResponse()

class DummyResponse(Response):
	def to_dict(self) -> dict:
		return {}
