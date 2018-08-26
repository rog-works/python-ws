# -*- coding: utf-8 -*-

import os
import re
import yaml
from errors.error import NotFoundError

class Config(object):
	def __init__(self, path: str = 'config/app.yml'):
		"""インスタンスを生成"""
		self._config = self.__load(self.__config_path(path))

	def __config_path(self, path: str) -> str:
		"""設定ファイルのファイルパスを取得

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

	def get(self, key: str):
		"""指定のキーに対応するを値を取得

		Args:
			key: キー

		Returns:
			設定値
		"""
		return self.__pluck(self._config, key.split('.'))

	def __pluck(self, root, routes: list) -> str:
		"""指定のキーに対応するを値を取得

		Args:
			root: 連想配列
			routes: ルート

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
