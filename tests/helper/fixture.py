# -*- coding: utf-8 -*-

def data_provider(data_provider_func):
	def decorator(test_func):
		def wrapper(self, *_):
			for args in data_provider_func():
				test_func(self, *args)
		return wrapper
	return decorator
