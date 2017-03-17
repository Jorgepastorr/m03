#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

salir = False
while salir == False:

	os.system('clear')
	var = raw_input(" 1-salir\n Que desea hacer: ")

	if var == "1":
		salir = True
				
	else:
		print "ninguna opcion correcta"
		tecla = raw_input("Pulse enter para continuar")
