# -*- config: utf-8 -*-

# from external.models.user import User
from net.request import Request
from di.di import inject
from error.errors import UnauthorizedError

class __Auth(object):
	def __init__(self):
		user = self.__signon()
		# if not user:
		# 	raise UnauthorizedError('Unauthorized')

		# self.user_id = user.ex_user_id
		# self.user_token = user.ex_user_token
		self.user_id = 100
		self.user_token = 'xxx'

	@inject('request')
	def __signon(self, request: Request): # -> User:
		pass
		# return User.get(
		# 	request.header('Authorization'),
		# 	request.header('X-Access-Token')
		# )

def authorize():
	return __Auth().__dict__

