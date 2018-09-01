# -*- coding: utf-8 -*-

import os
import re
import yaml
from error.errors import NotFoundError

class Config(object):
	"""コンフィグデータの読み込みと管理"""

	def __init__(self, path: str):
		"""インスタンスを生成

		:param str path: コンフィグファイルの相対パス
		"""
		self._config = self.__load(self.__config_path(path))

	def __config_path(self, path: str) -> str:
		"""設定ファイルの絶対パスを取得

		:param str path: 設定ファイルの相対パス
		:return str: 設定ファイルの絶対パス
		"""
		return os.path.abspath(f'{os.getcwd()}/{path}')

	def __load(self, path: str) -> dict:
		"""設定ファイルをロード

		:param str path: 設定ファイルの絶対パス
		:return str: 連想配列
		:raise NotFoundError: 設定ファイルが存在しない
		"""
		if not os.path.exists(path):
			raise NotFoundError(f'Not found configuretion file. path = "{path}"')

		f = open(path)
		data = yaml.load(f)
		f.close()
		return data

	def get(self, route: str):
		"""指定の参照パスに対応するデータを取得

		:param str route: 参照パス
		:return any: データ
		"""
		return self.__pluck(self._config, route.split('.'))

	def __pluck(self, root, routes: list):
		"""指定の参照パスに対応するデータを取得

		:param: dict|list root: 参照ルート
		:param: list routes: 参照キーリスト
		:return any: データ
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
