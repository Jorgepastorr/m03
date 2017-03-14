#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

while True:

	os.system('clear')
	var = input(" 1-Sumar\n 2-Restar\n 3-salir\n Que desea hacer: ") 

	if var == 1:
		num1 = input("introduce el primer numero: ")
		num2 = input("introduce el segundo numero: ")
		res = num1 + num2
		print "resultado de",num1,"+",num2,"es:",res
		tecla = raw_input("Pulse enter para continuar")
	
	elif var == 2:
		num1 = input("introduce el primer numero: ")
		num2 = input("introduce el segundo numero: ")
		res = num1 - num2
		print "resultado de",num1,"-",num2,"es:",res
		tecla = raw_input("Pulse enter para continuar")
		
	elif var == 3:
		break 	
	else:
		print "ninguna opcion correcta"
		tecla = raw_input("Pulse enter para continuar")
