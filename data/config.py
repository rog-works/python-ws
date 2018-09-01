# -*- coding: utf-8 -*-

import os
import re
import yaml
from error.errors import NotFoundError

class Config(object):
	def __init__(self, path: str):
		"""インスタンスを生成"""
		self._config = self.__load(self.__config_path(path))

	def __config_path(self, path: str) -> str:
		"""設定ファイルの絶対パスを取得

		Args:
			path: 設定ファイルの相対パス

		Returns:
			設定ファイルの絶対パス
		"""
		return os.path.abspath(f'{os.getcwd()}/{path}')

	def __load(self, path: str) -> dict:
		"""設定ファイルをロード

		Args:
			path: 設定ファイルの絶対パス

		Returns:
			連想配列

		Raises:
			NotFoundError: 設定ファイルが存在しない
		"""
		if not os.path.exists(path):
			raise NotFoundError(f'Not found configuretion file. path = "{path}"')

		f = open(path)
		data = yaml.load(f)
		f.close()
		return data

	def get(self, route: str):
		"""指定の参照パスに対応する設定値を取得

		Args:
			route: 参照パス

		Returns:
			設定値
		"""
		return self.__pluck(self._config, route.split('.'))

	def __pluck(self, root, routes: list) -> str:
		"""指定の参照パスに対応する設定値を取得

		Args:
			root: 参照ルート
			routes: 参照キーリスト

		Returns:
			設定値
		"""
		key = routes[0]
		if type(root) is list:
			if not re.match(r'^[\d]+$', key):
				return None
			key = int(key)

		if type(root) is list and len(root) <= key:
			return None
		if type(root) is dict and key not in root:
			return None

		if len(routes) == 1:
			return root[key]
		else:
			return self.__pluck(root[key], routes[1:])
