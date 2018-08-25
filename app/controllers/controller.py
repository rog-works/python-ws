# -*- coding: utf-8 -*-

from api.request import Request
from api.response import Response

class Controller:
	def __init__(self):
		self._request = None

	def initialize(self, request: Request):
		self._request = request

	@property
	def request(self) -> Request:
		return self._request

	def json(self, data: dict) -> Response:
		return Response(data)
