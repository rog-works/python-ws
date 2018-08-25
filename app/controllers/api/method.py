# -*- coding: utf-8 -*-

from api.request import Request

class Method:
	def before(self, req: Request):
		print('invoked #before')

	def after(self, result) -> dict:
		print('invoked #after')
		return result

	def show(self, req: Request) -> dict:
		print('invoked #show')
		return {}

