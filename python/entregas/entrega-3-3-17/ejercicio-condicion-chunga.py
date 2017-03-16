# !/usr/bin/python
# -*-coding: utf-8-*-
import os
os.system('clear')


print "Juego de pruebas: \nNumero negativo, par y entre -10 y 40 \n"
var = input("Introduce un número: ")


if (((var %2==0 and var >=-10) and var <= 40) and var < 0 ):
	print "Condición superada "
else:
	print "Eres un inutil vuelve a parvulitos"

