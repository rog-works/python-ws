# -*- coding: utf-8 -*-

from api.request import Builder

class Application:
	def __init__(self, event: dict):
		self._request = self.__to_request(event)

	def __to_request(self, event: dict):
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

	def run(self):
		action = Router().dispatch(self._request.url)
		action.execute(self._request)
