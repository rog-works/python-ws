# -*- config: utf-8 -*-

from external.models.user import User
from net.request import Request
from di.di import inject
from errors.error import UnauthorizationError

class Auth(object):
	def __init__(self):
		user = self.__signon()
		if not user:
			raise UnauthorizationError('Unauthorized')

		self._user_id = user.id
		self._user_token = user.token

	@inject('request')
	def __signon(self, request: Request) -> User:
		return User.get(
			request.header('Authorization'),
			request.header('X-Access-Token')
		)

