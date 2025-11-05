
def foo ():
	"""Erro de estilo (E): espaço desnecessário"""
	print ( 'Espaço desnecessário' )


def bar():
		"""Aviso de estilo (W): indentação incorreta"""
	x=1
	return  x


def unused_var():
	"""Pyflakes (F): variável não usada"""
	a = 10
	return 5


def bugbear_example():
	"""Bugbear (B): exceção genérica"""
	try:
		1/0
	except Exception:
		pass


import os
import sys
import re


def no_docstring():
	"""Docstring ausente (D)"""
	pass


def insecure():
	"""Segurança (S): uso de eval"""
	eval('2+2')


def complex_func(x):
	"""Complexidade ciclomática (C90): função complexa"""
	if x == 1:
		if x > 0:
			if x < 10:
				if x != 5:
					if x % 2 == 0:
						if x % 3 == 0:
							if x % 5 == 0:
								if x % 7 == 0:
									return True
	return False
