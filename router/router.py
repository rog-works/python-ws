# -*- coding: utf-8 -*-

import os
import importlib
import re
import yaml
from errors.error import NotFoundError, IndexOutOfBoundError, DataFormatError

class Router(object):
	"""ルーティング定義の管理と、ハンドラーの導出"""

	def __init__(self, path: str = 'config/routes.yml'):
		"""インスタンスを生成"""
		self._routes = self.__load(self.__routes_path(path))

	def __routes_path(self, path: str) -> str:
		"""ルーティング定義ファイルの絶対パスを取得

		Args:
			path: 定義ファイルの相対パス

		Returns:
			定義ファイルの絶対パス
		"""
		return os.path.abspath(f'{os.getcwd()}/{path}')

	def __load(self, path: str) -> dict:
		"""ルーティング定義ファイルをロード

		Args:
			path: 定義ファイルの絶対パス

		Returns:
			ルーティング定義の連想配列

		Raises:
			NotFoundError: ルーティング定義ファイルが存在しない
		"""
		if not os.path.exists(path):
			raise NotFoundError(f'Not found route configuretion. path = "{path}"')

		f = open(path)
		data = yaml.load(f)
		f.close()

		self.__validate_routes(data)
		return data

	def __validate_routes(self, routes: dict):
		"""ルーティング定義をバリデーション

		Args:
			routes: ルーティング定義

		Raises:
			DataFormatError: ハンドラー定義が不正
		"""
		for key, value in routes.items():
			if not re.match(r'^[\w.]+#[\w]+\.[\w]+$', value):
				raise DataFormatError(f'Unexpected route deffinition. deffinition = "{value}"')

	def __resolveDeffinition(self, route: str) -> tuple:
		"""ルートに対応するハンドラー定義を取得

		Args:
			route: ルート

		Returns:
			ハンドラー定義のタプル

		Raises:
			IndexOutBoundError: 定義に存在しないルート
		"""
		if not route in self._routes:
			raise IndexOutOfBoundError(f'Undefined route. route = "{route}"')

		deffinition = self._routes[route]
		module, handler = deffinition.split('#')
		klass, method = handler.split('.')
		return module, klass, method

	def __resolveHander(self, module: str, klass: str, method: str) -> tuple:
		"""指定のハンドラー定義からオブジェクトとハンドラーを取得

		Args:
			module: モジュールパス
			klass: クラス名
			method: メソッド名

		Returns:
			オブジェクトとハンドラーのタプル
		
		Raises:
			NotFoundError: ハンドラーが存在しない
		"""
		try:
			mod = importlib.import_module(module)
			obj = getattr(mod, klass)()
			handler = getattr(obj, method)
			return obj, handler
		except Exception as e:
			raise NotFoundError(f'Undefined handler. hander = {klass}.{method}, error = {e}')

	def dispatch(self, route: str) -> tuple:
		"""指定のルートからオブジェクトとハンドラーを取得

		Args:
			route: ルート

		Returns:
			オブジェクトとハンドラーのタプル
		"""
		deffinition = self.__resolveDeffinition(route)
		return self.__resolveHander(*deffinition)
