#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

salir = False
while salir == False:

	os.system('clear')	
	print "Menu de una calculadora:"	
	print "S - Salir"
	print "1 - Sumar"
	print "2 - Restar"
	print "3 - Multiplicar"
	print "4 - Dividir"
	num = raw_input(" Qué desea hacer el amo? ")

	if num == "S" or num == "s":
		print "¡Adios!"
		salir = True
	
	else:
		if num == "1":
			print "Sumar"
			print
			num1 = input("introduce el primer numero: ")
			num2 = input("introduce el segundo numero: ")
			res = num1 + num2
			print "resultado de",num1,"+",num2,"es:",res
			print
			tecla = raw_input("Pulse enter para continuar")
			
		else:
			if num == "2":
				print "Restar"
				print
				num1 = input("introduce el primer numero: ")
				num2 = input("introduce el segundo numero: ")
				res = num1 - num2
				print "resultado de",num1,"-",num2,"es:",res
				tecla = raw_input("Pulse enter para continuar")
				
			else:
				if num == "3":
					print "Miltiplicar"
					print
					num1 = input("introduce el primer numero: ")
					num2 = input("introduce el segundo numero: ")
					res = num1 * num2
					print "resultado de",num1,"*",num2,"es:",res
					tecla = raw_input("Pulse enter para continuar")
					
				else:
					if num == "4":
						print "Dividir"
						print
						num1 = input("introduce el primer numero: ")
						num2 = input("introduce el segundo numero: ")
						res = num1 / num2
						print "resultado de",num1,"/",num2,"es:",res
						tecla = raw_input("Pulse enter para continuar")
						
					else:
						print "Esta opción no existe"
						print
						tecla = raw_input("Pulse enter para continuar")



