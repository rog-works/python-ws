# -*- coding: utf-8 -*-

from di.container import Container as DI

class Model(object):
	@classmethod
	def api(cls):
		return DI.instance.get('api')

