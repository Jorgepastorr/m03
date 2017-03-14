#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
salir = raw_input("")

while salir False:

	os.system('clear')
	var = input(" 1-Sumar\n 2-Restar\n 3-salir\n Que desea hacer: ")


	if var == 1:
		print "opcion 1 suma"
		tecla = raw_input("Pulse enter para continuar")
	
	elif var == 2:
		print "opcion 2 resta"
		tecla = raw_input("Pulse enter para continuar")
	elif var == 3:
		salir = True
	else:
		print "ninguna opcion correcta"
		tecla = raw_input("Pulse enter para continuar")
