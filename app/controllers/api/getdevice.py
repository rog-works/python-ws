# -*- coding: utf-8 -*-

from api.request import Request
from api.response import Response
from app.controllers.controller import Controller

class GetDevice(Controller):
	def before(self):
		print(f'invoked #before via = {self.action.name}')

	def after(self, response: Response) -> Response:
		print('invoked #after')
		return response

	def show(self) -> Response:
		print('invoked #show')
		return self.json({'scceed': True})
