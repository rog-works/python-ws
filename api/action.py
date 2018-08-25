# -*- coding: utf-8 -*-

class Action(object):
	"""ハンドラーの管理と、ハンドリングの一連の操作を実行

	Attributes:
		_obj: ハンドラーオブジェクト
		_handler: ハンドラー
	"""

	def __init__(self, obj, handler):
		"""インスタンスを生成

		Args:
			obj: ハンドラーオブジェクト
			handler: ハンドラー
		"""
		self._obj = obj
		self._handler = handler

	@property
	def name(self) -> str:
		"""ハンドラーの名前を取得するプロパティ

		Returns:
			ハンドラーの名前
		"""
		return self._handler.__name__

	def __before(self):
		"""ハンドラーの事前処理を実行。定義されていない場合は何もしない"""
		if hasattr(self._obj, 'before'):
			self._obj.before()

	def __after(self, response):
		"""ハンドラーの事後処理を実行。定義されていない場合は何もしない

		Args:
			response: レスポンス

		Returns:
			レスポンス
		"""
		if hasattr(self._obj, 'after'):
			return self._obj.after(response)
		else:
			return response

	def initialize(self, *args):
		"""
		ハンドラーオブジェクトの初期化処理を実行。定義されていない場合は何もしない

		Args:
			*args: 初期化用引数
		"""
		if hasattr(self._obj, 'initialize'):
			self._obj.initialize(*args)

	def execute(self):
		"""ハンドラーを実行し、レスポンスを返却

		Returns:
			レスポンス
		"""
		self.__before()
		response = self._handler()
		return self.__after(response)
