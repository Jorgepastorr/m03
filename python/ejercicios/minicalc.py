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
			os.system('clear')
			print "Sumar"
			print
			num1 = input("introduce el primer numero: ")
			num2 = input("introduce el segundo numero: ")
			res = num1 + num2
			print "resultado de",num1,"+",num2,"es:",res
			print
			tecla = raw_input("Pulse enter para continuar")
			############# memnu para seguir sumando ############################
			
			sal = False
			while sal == False:
				
				os.system('clear')
				opcion = raw_input("Quiere seguir sumando [ si - no ]: ")
				if opcion == "si" or opcion == "SI":
					os.system('clear')
					num3 = input("Inserte el número ")				
					res = res + num3 
					print "El resultado sumandole",num3,"es:",res
					print
					tecla = raw_input("Pulse enter para continuar")
					
				else:
					if opcion == "no" or opcion == "NO":
						sal = True
						tecla = raw_input("Volvera al menu inicial")
					else:
						tecla1 = raw_input("Opcion incorrecta")
			####################################
		else:
			if num == "2":
				print "Restar"
				print
				num1 = input("Introduce el primer numero: ")
				num2 = input("Introduce el segundo numero: ")
				res = num1 - num2
				print "resultado de",num1,"-",num2,"es:",res
				tecla = raw_input("Pulse enter para continuar")
				############# memnu para seguir restando ############################
				sal = False
				while sal == False:
					
					os.system('clear')
					opcion = raw_input("Quiere seguir restando [ si - no ]: ")
					if opcion == "si" or opcion == "SI":
						os.system('clear')
						num3 = input("Inserte el número ")
						res = res - num3 
						print "El resultado restandole",num3,"es:",res
						print
						tecla = raw_input("Pulse enter para continuar")
						
					else:
						if opcion == "no" or opcion == "NO":
							sal = True
							tecla = raw_input("Volvera al menu inicial")
						else:
							tecla1 = raw_input("Opcion incorrecta")
				####################################
			else:
				if num == "3":
					print "Miltiplicar"
					print
					num1 = input("introduce el primer numero: ")
					num2 = input("introduce el segundo numero: ")
					res = num1 * num2
					print "resultado de",num1,"*",num2,"es:",res
					tecla = raw_input("Pulse enter para continuar")
		############# memnu para seguir multiplicando ############################
					sal = False
					while sal == False:
						
						os.system('clear')
						opcion = raw_input("Quiere seguir multiplicando [ si - no ]: ")
						if opcion == "si" or opcion == "SI":
							os.system('clear')
							num3 = input("Inserte el número ")
							res = res * num3 
							print "El resultado multiplicandole",num3,"es:",res
							print
							tecla = raw_input("Pulse enter para continuar")
			
						else:
							if opcion == "no" or opcion == "NO":
								sal = True
								tecla = raw_input("Volvera al menu inicial")
							else:
								tecla1 = raw_input("Opcion incorrecta")
					####################################
				else:
					if num == "4":
						print "Dividir"
						print
						num1 = input("introduce el primer numero: ")
						num2 = input("introduce el segundo numero: ")
						res = num1 / num2
						print "resultado de",num1,"/",num2,"es:",res
						tecla = raw_input("Pulse enter para continuar")
				############# memnu para seguir dividiendo ############################
						sal = False
						while sal == False:
							
							os.system('clear')
							opcion = raw_input("Quiere seguir dividiendo [ si - no ]: ")
							if opcion == "si" or opcion == "SI":
								os.system('clear')
								num3 = input("Inserte el número ")
								res = res / num3 
								print "El resultado dividiendole",num3,"es:",res
								print
								tecla = raw_input("Pulse enter para continuar")
							
							else:
								if opcion == "no" or opcion == "NO":
									sal = True
									tecla = raw_input("Volvera al menu inicial")
								else:
									tecla1 = raw_input("Opcion incorrecta")
						####################################						
					else:
						print "Esta opción no existe"
						print
						tecla = raw_input("Pulse enter para continuar")



