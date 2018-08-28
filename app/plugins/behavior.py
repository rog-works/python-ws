# -*- coding: utf-8 -*-

def behavior(before = None, after = None):
	def decorator(wrapper_func):
		def wrapper(self, *args):
			if before:
				before(self, *args)
			data = wrapper_func(self, *args)
			if after:
				return after(self, data)
			else:
				return data
		return wrapper
	return decorator
