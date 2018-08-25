# -*- coding: utf-8 -*-

from api.action import Action
from api.request import Request
from api.response import Response

class Controller:
	def __init__(self):
		self._action = None
		self._request = None

	def initialize(self, action: Action, request: Request):
		self._action = action
		self._request = request

	@property
	def action(self) -> Action:
		return self._action

	@property
	def request(self) -> Request:
		return self._request

	def json(self, data: dict) -> Response:
		return Response(data)
