# -*- coding: utf-8 -*-

from api.router import Router
from api.request import Request, Builder
from api.response import Response
from api.action import Action

class Application:
	def __build_request(self, event: dict) -> Request:
		builder = Builder()
		if 'url' in event:
			builder.url(event['url'])
		if 'headers' in event:
			builder.headers(event['headers'])
		if 'query' in event:
			builder.query(event['query'])
		if 'body' in event:
			builder.body(event['body'])
		return builder.build()

	def run(self, event) -> Response:
		request = self.__build_request(event)
		action = Action(*Router().dispatch(request.url))
		action.initialize(request)
		return action.execute()
