import sys

PI = 3.14159  # Constante

def area_circulo(r):
	"""Exemplo de cálculo de área de círculo"""
	return PI * r ** 2  # noqa: E501

def funcao_com_erro_de_indentacao():
print("Erro de indentação")  # noqa: E901

def funcao_com_espacos_em_branco():    
	x = 1    
	return x  # noqa: W291

def funcao_com_nome_errado():
	pass  # noqa: N802

def funcao_com_import_nao_usado():
	import math  # noqa: F401

def funcao_com_variavel_nao_usada():
	y = 2  # noqa: F841
	return 1

def funcao_com_dupla_importacao():
	import sys  # noqa: F811

def funcao_com_linha_muito_longa():
	return "Esta é uma linha muito longa que ultrapassa o limite de 88 caracteres do ruff, apenas para testar o erro."  # noqa: E501
