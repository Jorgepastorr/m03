#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

salir = False
while salir == False:

	os.system('clear')	
	print "*-Menu de una calculadora y bucle principal-*"	
	print "S - Salir"
	print "1 - Bucle while salir == false"
	print "2 - Bucle while not salir"
	print "3 - Multiplicar"
	print "4 - Dividir"
	num = raw_input(" Qué desea hacer el amo? ")

	if num == "S" or num == "s":
		print "¡Adios!"
		salir = True
	
	else:
		if num == "1":
			sali = False
			while sali == False:

				os.system('clear')
				var = raw_input(" *-Sub bucle1-*\n 1-salir\n 2-Sub bucle2\n Que desea hacer: ")

				if var == "1":
					sali = True
				else:
					if var =="2":
						salire = False
						while salire == False:

							os.system('clear')
							var = raw_input(" *-Sub bucle2-*\n 1-salir\n Que desea hacer: ")

							if var == "1":
								salire = True
										
							else:
								print "ninguna opcion correcta"
								tecla = raw_input("Pulse enter para continuar")
				
					else:
						print "ninguna opcion correcta"
						tecla = raw_input("Pulse enter para continuar")

			
		else:
			if num == "2":
				sal = False
				while not sal:

					os.system('clear')
					var = raw_input(" Me gusta mas esta manera de entrar en bucle\n 1-salir\n Que desea hacer: ")

					if var == "1":
						sal = True
								
					else:
						print "ninguna opcion correcta"
						tecla = raw_input("Pulse enter para continuar")

				
			else:
				if num == "3":
					print "Miltiplicar"
					print
					tecla = raw_input("Pulse enter para continuar")
					
				else:
					if num == "4":
						print "Dividir"
						print
						tecla = raw_input("Pulse enter para continuar")
						
					else:
						print "Esta opción no existe"
						print
						tecla = raw_input("Pulse enter para continuar")
