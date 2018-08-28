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
		self._routes = self.__load_routes(self.__routes_path(path))

	def __routes_path(self, path: str) -> str:
		"""ルーティング定義ファイルの絶対パスを取得

		Args:
			path: 定義ファイルの相対パス

		Returns:
			定義ファイルの絶対パス
		"""
		return os.path.abspath(f'{os.getcwd()}/{path}')

	def __load_routes(self, path: str) -> dict:
		"""ルーティング定義ファイルをロード

		Args:
			path: 定義ファイルの絶対パス

		Returns:
			ルーティング定義の連想配列

		Raises:
			NotFoundError: ルーティング定義ファイルが存在しない
			DataFormatError: ハンドラー定義が不正
		"""
		if not os.path.exists(path):
			raise NotFoundError(f'Not found route configuretion. path = "{path}"')

		f = open(path)
		data = yaml.load(f)
		f.close()

		if not self.__validate_routes(data):
			raise DataFormatError(f'Unexpected route deffinition. deffinition = "{value}"')

		return data

	def __validate_routes(self, routes: dict) -> bool:
		"""ルーティング定義をバリデーション

		Args:
			routes: ルーティング定義

		Returns:
			True = 正常
		"""
		for key, value in routes.items():
			if not re.match(r'^[\w.]+#[\w]+\.[\w]+$', value):
				return False

		return True

	def __resolveDeffinition(self, route: str) -> tuple:
		"""ルートに対応するハンドラー定義を取得

		Args:
			route: ルート

		Returns:
			ハンドラー定義のタプル

		Raises:
			RouteMissmatchError: 定義に存在しないルート
		"""
		if not route in self._routes:
			raise RouteMissmatchError(f'Undefined route. route = "{route}"')

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

	def resolve(self, route: str) -> 'Dispatcher':
		"""指定のルートに対応するハンドラーへのディスパッチャーを取得

		Args:
			route: ルート

		Returns:
			ディスパッチャー
		"""
		deffinition = self.__resolveDeffinition(route)
		return Dispatcher(*self.__resolveHander(*deffinition))

class Dispatcher(object):
	"""ハンドラーの管理と、ハンドリングの一連の操作を実行"""

	def __init__(self, class_type: type, method_name: str):
		"""インスタンスを生成

		Args:
			class_type: クラスタイプ
			method_name: メソッド名
		"""
		self._class_type = class_type
		self._method_name = method_name

	def instantiate(self, *args):
		"""
		ハンドラーを生成

		Args:
			*args: コンストラクタ用引数

		Returns:
			ハンドラー

		Raises:
			RouteMissmatchError: ハンドラーメソッドが存在しない
		"""
		try:
			obj = self._class_type(*args)
			return getattr(obj, self._method_name)
		except AttributeError as e:
			raise RouteMissmatchError(f'Undefined method. handler = "{self._class_type.__name__}.{self._method_name}", message = {e}')
