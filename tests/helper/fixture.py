# -*- coding: utf-8 -*-

def data_provider(data_provider_func):
	"""テストメソッドに引数を注入する

	:example:
		@data_provider(lambda : [
			(1, 2, 3),
		])
		def test_method(self, arg1, arg2, arg3):
			pass

	:param function data_provider_func: 引数を生成する関数
	"""
	def decorator(test_func):
		def wrapper(self, *_):
			for args in data_provider_func():
				test_func(self, *args)
		return wrapper
	return decorator
