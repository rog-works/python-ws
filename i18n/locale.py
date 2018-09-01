# -*- coding: utf-8 -*-

from data.config import Config
from error.errors import NotFoundArgumentError

class Locale(object):
	"""言語毎の翻訳データの管理と、翻訳"""

	def __init__(self, lang: str):
		"""インスタンスを生成

		:param str lang: 言語キー
		"""
		self._lang = lang
		self._transes = {}
	
	def __trans_path(self, lang: str, category: str) -> str:
		"""翻訳定義ファイルの相対パスを取得

		:param str lang: 言語キー
		:param str category: 翻訳定義ファイルの種類
		:return str: 翻訳定義ファイルの相対パス
		"""
		return f'i18n/{lang}/{category}.yml'

	def __load_config(self, category: str) -> Config:
		"""翻訳定義ファイルをロード

		:param str category: 翻訳定義ファイルの種類
		:return Config: 翻訳データのコンフィグ
		:raise NotFoundError: 翻訳定義ファイルが存在しない
		"""
		return Config(self.__trans_path(self._lang, category))

	def trans(self, route: str) -> str:
		"""指定のキーに対応する翻訳語の文字列を取得

		:param str route: 参照パス
		:return str: 翻訳後の文字列
		:raise NotFoundError: 指定の翻訳データが存在しない
		"""
		category, *routes = route.split('.')
		if category not in self._transes:
			self._transes[category] = self.__load_config(category)

		trans = self._transes[category].get('.'.join(routes))
		if not trans:
			raise NotFoundError(f'Undefined translate. route = {route}')

		return trans
