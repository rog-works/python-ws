# -*- coding: utf-8 -*-

from errors.error import NotFoundError

class Action(object):
	"""ハンドラーの管理と、ハンドリングの一連の操作を実行"""

	def __init__(self, class_type: type, method_name: str):
		"""インスタンスを生成

		Args:
			class_type: クラスタイプ
			method_name: メソッド名
		"""
		self._class_type = class_type
		self._method_name = method_name
		self._obj = None

	def instantiate(self, *args):
		"""
		ハンドラーオブジェクトを生成

		Args:
			*args: コンストラクタ用引数
		"""
		self._obj = self._class_type(*args)

	def execute(self):
		"""ハンドラーを実行し、レスポンスを返却

		Returns:
			レスポンス

		Raises:
			NotFoundError: ハンドラーメソッドが存在しない
		"""
		try:
			if not self._obj:
				self.instantiate()

			handler = getattr(self._obj, self._method_name)
			return handler()
		except AttributeError as e:
			raise NotFoundError(f'Undefined method. handler = "{self._class_type.__name__}.{self._method_name}", message = {e}')
