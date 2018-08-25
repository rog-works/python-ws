# -*- coding: utf-8 -*-

from api.request import Request
from api.response import Response
from app.controllers.controller import Controller

class GetDevice(Controller):
	def before(self):
		print('invoked #before')

	def after(self, res: Response) -> Response:
		print('invoked #after')
		return self.json({'scceed': True})

	def show(self) -> Response:
		print('invoked #show')
		return {}
