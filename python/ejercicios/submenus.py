#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
salir = False

while not salir:

	os.system('clear')
	var = raw_input(" Menu principal\n 1-Submenubreak\n 2-Submenu var false\n 3-salir\n Que desea hacer: ")


	if var == "1":
		while True:
			os.system('clear')
			op = raw_input("1-salir \nEsta en el submenu 1: ")
			if op == "1":
				break
			else:
				print "No hay mas opciones"
				tecla = raw_input("Pulse enter para continuar")
	
	elif var == "2":
		sal = False
		while not sal:
			os.system('clear')
			op = raw_input("1-salir \nEsta en el submenu 2: ")
			if op == "1":
				sal = True
			else:
				print "No hay mas opciones"
				tecla = raw_input("Pulse enter para continuar")
	
	
	elif var == "3":
		salir = True
	
	else:
		print "ninguna opcion correcta"
		tecla = raw_input("Pulse enter para continuar")
