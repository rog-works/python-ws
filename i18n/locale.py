# -*- coding: utf-8 -*-

import os
import yaml
from data.config import Config
from errors.error import IllegalArgumentError

class Locale(object):
	"""言語毎の翻訳データの管理と、翻訳"""

	def __init__(self, lang: str):
		"""インスタンスを生成

		Args:
			lang: 言語キー
		"""
		self._lang = lang
		self._transes = {}
	
	def __trans_path(self, lang: str, category: str) -> str:
		"""翻訳定義ファイルの相対パスを取得

		Args:
			lang: 言語キー
			category: 翻訳定義ファイルの種類

		Returns:
			翻訳定義ファイルの相対パス
		"""
		return f'i18n/{lang}/{category}.yml'

	def __load_config(self, category) -> Config:
		"""翻訳定義ファイルをロード

		Args:
			lang: 言語キー
			category: 翻訳定義ファイルの種類

		Returns:
			翻訳データのコンフィグ

		Raises:
			NotFoundError: 翻訳定義ファイルが存在しない
		"""
		return Config(self.__trans_path(self._lang, category))

	def trans(self, route: str) -> str:
		"""指定のキーに対応するを翻訳データを取得

		Args:
			route: 参照パス

		Returns:
			翻訳後の文字列

		Raises:
			IllegalArgumentError: 指定の翻訳データが存在しない
		"""
		category, *routes = route.split('.')
		if category not in self._transes:
			self._transes[category] = self.__load_config(category)

		trans = self._transes[category].get('.'.join(routes))
		if not trans:
			raise IllegalArgumentError(f'Undefined translate. route = {route}')

		return trans
