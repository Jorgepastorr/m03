#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
os.system('clear')

print "Menu de una calculadora:"	
print "S - Salir"
print "1 - Sumar"
print "2 - Restar"
print "3 - Multiplicar"
print "4 - Dividir"
num = raw_input(" Qué desea hacer el amo? ")
print


if ( num >= "1" and num <= "4" ) or num == "S" or num == "s":
	print "opciones correctas"
else:
	print "Esa opción no existe"
