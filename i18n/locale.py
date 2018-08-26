# -*- coding: utf-8 -*-

import os
import yaml
from errors.error import NotFoundError, IllegalArgumentError

class Locale(object):
	"""言語毎の翻訳データの管理と、マッピング"""

	def __init__(self, lang: str):
		"""イベントデータからリクエストを生成

		Args:
			lang: 言語キー
		"""
		self._lang = lang
		self._transes = {}
	
	def __trans_path(self, lang: str, category: str) -> str:
		"""翻訳ファイルのファイルパスを取得

		Args:
			lang: 言語キー
			category: 翻訳ファイルの種類

		Returns:
			翻訳ファイルのパス
		"""
		return os.path.join(os.getcwd(), 'locale', lang, f'{category}.yml')

	def __load(self, category) -> dict: 
		"""翻訳ファイルをロード

		Args:
			lang: 言語キー
			category: 翻訳ファイルの種類

		Returns:
			翻訳データの連想配列

		Raises:
			NotFoundError: 翻訳ファイルが存在しない
		"""
		path = self.__trans_path(self._lang, category)
		if not os.path.exists(path):
			raise NotFoundError(f'Not found translate configure. language = {self._lang}, category = {category}')

		f = open(path)
		data = yaml.load(path)
		f.close()
		return data

	def trans(self, route: str) -> str:
		"""指定のキーに対応するを翻訳データを取得

		Args:
			routes: キー

		Returns:
			翻訳後の文字列

		Raises:
			IllegalArgumentError: 指定の翻訳データが存在しない
		"""
		category, *routes = route.split('.')
		if not category in self._transes:
			self._transes[category] = self.__load(self.__trans_path(category))

		trans = self.__resolve(self._transes[category], routes)
		if not trans:
			raise IllegalArgumentError(f'Undefined translate. route = {route}')

		return trans

	def __resolve(self, root: dict, routes: list) -> str:
		"""指定のキーに対応するを翻訳データを取得

		Args:
			root: 翻訳データの連想配列
			routes: ルート

		Returns:
			翻訳後の文字列
		"""
		if routes[0] in root:
			return ''

		if len(routes):
			return root[routes[0]]
		else:
			return self.__resolve(root[routes[0]], routes[1:])
