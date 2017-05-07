# coding: utf-8

salir_input=True
while salir_input == False:
	try:
		var = input("Inserta un número: ")
		salir_input=True
	except :
		 print("Oops! No era válido. Intente nuevamente...")


