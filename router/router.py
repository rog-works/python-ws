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
		module_path, handler = deffinition.split('#')
		class_name, method_name = handler.split('.')
		return module_path, class_name, method_name

	def __resolveHander(self, module_path: str, class_name: str, method_name: str) -> tuple:
		"""指定のハンドラー定義からクラスタイプとメソッド名を取得

		Args:
			module_path: モジュールパス
			class_name: クラス名
			method_name: メソッド名

		Returns:
			クラスタイプとメソッド名のタプル
		
		Raises:
			NotFoundError: ハンドラーが存在しない
		"""
		try:
			module = importlib.import_module(module_path)
			class_type = getattr(module, class_name)
			return class_type, method_name
		except AttributeError as e:
			raise NotFoundError(f'Undefined handler. hander = {class_name}.{method_name}, message = {e}')

	def dispatch(self, route: str) -> tuple:
		"""指定のルートに対応するハンドラーのクラスタイプとメソッド名を取得

		Args:
			route: ルート

		Returns:
			クラスタイプとメソッド名のタプル
		"""
		deffinition = self.__resolveDeffinition(route)
		return self.__resolveHander(*deffinition)
