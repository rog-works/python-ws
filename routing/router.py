# -*- coding: utf-8 -*-

import os
import importlib
import re
import yaml
from error.errors import NotFoundError, DataFormatError, RouteMissmatchError

class Router(object):
	"""ルーティング定義の読み込み・管理と、ハンドラーの導出"""

	def __init__(self, path: str = 'config/routes.yml'):
		"""インスタンスを生成

		:param str path: ルーティング定義ファイルの相対パス
		"""
		self._routes = self.__load_routes(self.__routes_path(path))

	def __routes_path(self, path: str) -> str:
		"""ルーティング定義ファイルの絶対パスを取得

		:params str path: 定義ファイルの相対パス
		:return str: 定義ファイルの絶対パス
		"""
		return os.path.abspath(f'{os.getcwd()}/{path}')

	def __load_routes(self, path: str) -> dict:
		"""ルーティング定義ファイルをロード

		:param str path: 定義ファイルの絶対パス
		:return dict: ルーティング定義の連想配列
		:raise NotFoundError: ルーティング定義ファイルが存在しない
		:raise DataFormatError: ハンドラー定義が不正
		"""
		if not os.path.exists(path):
			raise NotFoundError(f'Not found route configuretion. path = "{path}"')

		with open(path) as f:
			data = yaml.load(f)

		if not self.__validate_routes(data):
			raise DataFormatError(f'Unexpected route deffinition. deffinition = "{value}"')

		return data

	def __validate_routes(self, routes: dict) -> bool:
		"""ルーティング定義をバリデーション

		:param dict routes: ルーティング定義
		:return bool: True = 正常
		"""
		for key, value in routes.items():
			if not re.match(r'^[\w.]+#[\w]+\.[\w]+$', value):
				return False

		return True

	def __resolveDeffinition(self, route: str) -> tuple:
		"""ルートに対応するハンドラー定義を取得

		:param str route: ルート
		:return tuple: ハンドラー定義のタプル
		:raise RouteMissmatchError: 定義に存在しないルート
		"""
		if not route in self._routes:
			raise RouteMissmatchError(f'Undefined route. route = "{route}"')

		deffinition = self._routes[route]
		module_path, handler = deffinition.split('#')
		class_name, method_name = handler.split('.')
		return module_path, class_name, method_name

	def __resolveHander(self, module_path: str, class_name: str, method_name: str) -> tuple:
		"""指定のハンドラー定義からクラスタイプとメソッド名を取得

		:param str module_path: モジュールパス
		:param str class_name: クラス名
		:param str method_name: メソッド名
		:return tuple: クラスタイプとメソッド名のタプル
		:raise RouteMissmatchError: ハンドラーが存在しない
		"""
		try:
			module = importlib.import_module(module_path)
			class_type = getattr(module, class_name)
			return class_type, method_name
		except AttributeError as e:
			raise RouteMissmatchError(f'Undefined handler. hander = {class_name}.{method_name}, message = {e}')

	def dispatch(self, route: str) -> 'Receiver':
		"""指定のルートに対応するハンドラーファクトリーを取得

		:param str route: ルート
		:return Receiver: ファクトリー
		:raise RouteMissmatchError: ハンドラーが存在しない
		"""
		deffinition = self.__resolveDeffinition(route)
		return Receiver(*self.__resolveHander(*deffinition))

class Receiver(object):
	"""ハンドラーを生成する"""

	def __init__(self, class_type: type, method_name: str):
		"""インスタンスを生成

		:param type class_type: クラスタイプ
		:param str method_name: メソッド名
		"""
		self._class_type = class_type
		self._method_name = method_name

	def instantiate(self, *args):
		"""ハンドラーを生成

		:param tuple *args: コンストラクタ用引数
		:return funtion: ハンドラー
		:raise RouteMissmatchError: ハンドラーメソッドが存在しない
		"""
		try:
			obj = self._class_type(*args)
			return getattr(obj, self._method_name)
		except AttributeError as e:
			raise RouteMissmatchError(f'Undefined method. handler = "{self._class_type.__name__}.{self._method_name}", message = {e}')
