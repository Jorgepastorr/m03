#!/usr/bin/env python
# -*- coding: utf-8 -*-

def control_casillas_originales(salir_raw):

	#### variables salia sudoku 1
	a1,a2,a3,a4,a5,a6,a7,a8,a9=0,8,0,0,0,0,0,0,0
	b1,b2,b3,b4,b5,b6,b7,b8,b9=9,5,0,0,6,0,7,0,4
	c1,c2,c3,c4,c5,c6,c7,c8,c9=3,0,0,0,0,0,0,0,9
	d1,d2,d3,d4,d5,d6,d7,d8,d9=0,2,0,0,0,0,0,0,0
	e1,e2,e3,e4,e5,e6,e7,e8,e9=0,0,4,0,0,5,0,0,0
	f1,f2,f3,f4,f5,f6,f7,f8,f9=7,1,0,0,0,2,9,4,0
	g1,g2,g3,g4,g5,g6,g7,g8,g9=0,6,8,0,2,0,0,7,3
	h1,h2,h3,h4,h5,h6,h7,h8,h9=0,0,0,4,5,0,6,0,8
	i1,i2,i3,i4,i5,i6,i7,i8,i9=4,0,2,6,3,0,0,9,5
	
	asignacion={"a1":a1,"a2":a2,"a3":a3,"a4":a4,"a5":a5,"a6":a6,"a7":a7,"a8":a8,"a9":a9,"b1":b1,"b2":b2,"b3":b3,"b4":b4,"b5":b5,"b6":b6,"b7":b7,"b8":b8,"b9":b9,"c1":c1,"c2":c2,"c3":c3,"c4":c4,"c5":c5,"c6":c6,"c7":c7,"c8":c8,"c9":c9,"d1":d1,"d2":d2,"d3":d3,"d4":d4,"d5":d5,"d6":d6,"d7":d7,"d8":d8,"d9":d9,"e1":e1,"e2":e2,"e3":e3,"e4":e4,"e5":e5,"e6":e6,"e7":e7,"e8":e8,"e9":e9,"f1":f1,"f2":f2,"f3":f3,"f4":f4,"f5":f5,"f6":f6,"f7":f7,"f8":f8,"f9":f9,"g1":g1,"g2":g2,"g3":g3,"g4":g4,"g5":g5,"g6":g6,"g7":g7,"g8":g8,"g9":g9,"h1":h1,"h2":h2,"h3":h3,"h4":h4,"h5":h5,"h6":h6,"h7":h7,"h8":h8,"h9":h9,"i1":i1,"i2":i2,"i3":i3,"i4":i4,"i5":i5,"i6":i6,"i7":i7,"i8":i8,"i9":i9}
	fila= raw_input("Inserta letra de fila ( Siempre en minusculas ): ")
	columna=raw_input("Inserta número de columna: ")
	# jumnta 2 variables en 1
	casilla=(fila+columna)

	if asignacion[casilla] != 0 :
		print "No puedes cambiar ese número. \nEs del sudoku original."
	else:	
		salir_raw=True

	return fila,columna,casilla,salir_raw

############3

def condiciones_de_entrada(salir,numero,fila,columna,si_completas,sudoku,condicion_entrada,fila_cambio_a_numero,columna_a_num,asignacion):
	
	# cuando todas las listas esten ordenadas del 1-9 ganas.
	if si_completas(A,B,C,D,E,F,G,H,I,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9):
		os.system('clear')
		print "¡¡ Felicidades !! Sin duda no tiene amigos."
		salir = True
		bucle=True
	else:
		# plantilla de salida
		sudoku(asignacion)
		print "salir: numero = -1"
	# control de error input
		salir_input=False
		while salir_input == False:
			try:
				numero = input("Inserta un número: ")
				salir_input=True
			except :
				 print("Oops! No era válido. Intente nuevamente...")
	#######
		salir_raw=False
		while salir_raw == False:
			if numero != -1:
				fila,columna,casilla,salir_raw = control_casillas_originales(salir_raw)	
			else:
				salir_raw=True
		
		bucle=False
		while bucle == False:
			
			if numero == -1:
				os.system('clear')
				print "Adios"
				salir = True
				bucle = True
		# si quieres jugar
			# condición para jugar (poner casilla y numero correcto)
			elif  condicion_entrada(fila,numero,columna,fila_cambio_a_numero,columna_a_num):
				bucle = True
				
			else:
		# posibles fallos
		############ revisar
				os.system('clear')
				if not (fila in fila_cambio_a_numero ):
					print "fila alfabética incorrecta"
				if not (columna in columna_a_num ):
					print "Columna numérica incorrecta"
				if numero < 1 or numero > 9 :
					print "número erroneo"
			###############3
				sleep (4)
				os.system('clear')

				sudoku(asignacion)
				print "salir: numero = -1"
			# control de error input
				salir_input=False
				while salir_input == False:
					try:
						numero = input("Inserta un número: ")
						salir_input=True
					except :
						 print("Oops! No era válido. Intente nuevamente...")
			
				salir_raw=False
				while salir_raw == False:
					if numero != -1:
						fila,columna,casilla,salir_raw = control_casillas_originales(salir_raw)	
					else:
						salir_raw=True
				
				
	
	return salir,numero,fila,columna,casilla

#################

salir,numero,fila,columna,casilla = condiciones_de_entrada(salir,numero,fila,columna,si_completas,sudoku,condicion_entrada,fila_cambio_a_numero,columna_a_num,asignacion)
