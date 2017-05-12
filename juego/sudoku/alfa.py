#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from time import sleep
os.system('clear')
#################################
#       variables
####################################3

############ listas ###############
## listas de lineas y recuadros
A,B,C,D,E,F,G,H,I=[8,0,0,0,0,0,0,0,0],[9,5,6,7,4,0,0,0,0],[3,9,0,0,0,0,0,0,0],[2,0,0,0,0,0,0,0,0],[4,5,0,0,0,0,0,0,0],[7,1,2,9,4,0,0,0,0],[6,8,2,7,3,0,0,0,0],[4,5,6,8,0,0,0,0,0],[4,2,6,3,9,5,0,0,0]
l1,l2,l3,l4,l5,l6,l7,l8,l9=[9,3,7,4,0,0,0,0,0],[8,5,2,1,6,0,0,0,0],[4,8,2,0,0,0,0,0,0],[4,6,0,0,0,0,0,0,0],[6,2,5,3,0,0,0,0,0],[5,2,0,0,0,0,0,0,0],[7,9,6,0,0,0,0,0,0],[4,7,9,0,0,0,0,0,0],[4,9,3,8,5,0,0,0,0]
r1,r2,r3,r4,r5,r6,r7,r8,r9=[8,9,5,3,0,0,0,0,0],[0,6,0,0,0,0,0,0,0],[7,4,9,0,0,0,0,0,0],[2,4,7,1,0,0,0,0,0],[5,2,0,0,0,0,0,0,0],[9,4,0,0,0,0,0,0,0],[0,6,8,4,2,0,0,0,0],[2,4,5,6,3,0,0,0,0],[7,3,6,8,9,5,0,0,0]


#################################

#### variables del panel
a1,a2,a3,a4,a5,a6,a7,a8,a9=0,8,0,0,0,0,0,0,0
b1,b2,b3,b4,b5,b6,b7,b8,b9=9,5,0,0,6,0,7,0,4
c1,c2,c3,c4,c5,c6,c7,c8,c9=3,0,0,0,0,0,0,0,9
d1,d2,d3,d4,d5,d6,d7,d8,d9=0,2,0,0,0,0,0,0,0
e1,e2,e3,e4,e5,e6,e7,e8,e9=0,0,4,0,0,5,0,0,0
f1,f2,f3,f4,f5,f6,f7,f8,f9=7,1,0,0,0,2,9,4,0
g1,g2,g3,g4,g5,g6,g7,g8,g9=0,6,8,0,2,0,0,7,3
h1,h2,h3,h4,h5,h6,h7,h8,h9=0,0,0,4,5,0,6,0,8
i1,i2,i3,i4,i5,i6,i7,i8,i9=4,0,2,6,3,0,0,9,5

#################################

###################################3
lista_columna={"1":l1,"2":l2,"3":l3,"4":l4,"5":l5,"6":l6,"7":l7,"8":l8,"9":l9}
lista_fila={"a":A,"b":B,"c":C,"d":D,"e":E,"f":F,"g":G,"h":H,"i":I}
fila_cambio_a_numero={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9}
columna_a_num={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

# DICCIONARIO asignación
asignacion={"a1":a1,"a2":a2,"a3":a3,"a4":a4,"a5":a5,"a6":a6,"a7":a7,"a8":a8,"a9":a9,"b1":b1,"b2":b2,"b3":b3,"b4":b4,"b5":b5,"b6":b6,"b7":b7,"b8":b8,"b9":b9,"c1":c1,"c2":c2,"c3":c3,"c4":c4,"c5":c5,"c6":c6,"c7":c7,"c8":c8,"c9":c9,"d1":d1,"d2":d2,"d3":d3,"d4":d4,"d5":d5,"d6":d6,"d7":d7,"d8":d8,"d9":d9,"e1":e1,"e2":e2,"e3":e3,"e4":e4,"e5":e5,"e6":e6,"e7":e7,"e8":e8,"e9":e9,"f1":f1,"f2":f2,"f3":f3,"f4":f4,"f5":f5,"f6":f6,"f7":f7,"f8":f8,"f9":f9,"g1":g1,"g2":g2,"g3":g3,"g4":g4,"g5":g5,"g6":g6,"g7":g7,"g8":g8,"g9":g9,"h1":h1,"h2":h2,"h3":h3,"h4":h4,"h5":h5,"h6":h6,"h7":h7,"h8":h8,"h9":h9,"i1":i1,"i2":i2,"i3":i3,"i4":i4,"i5":i5,"i6":i6,"i7":i7,"i8":i8,"i9":i9}


###################################3
#################################
#  niveles def
#################################
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
	
	# si la casilla es diferente a 0 no te deja insertar el númeo
	if asignacion[casilla] != 0 :
		print "No puedes cambiar ese número. \nEs del sudoku original."
	else:	
		salir_raw=True

	return fila,columna,casilla,salir_raw
	

############### asignacion buena ##################

def asignaciones(numero,fila,columna,casilla,lista_columna,lista_fila,fila_cambio_a_numero,columna_a_num,asignacion,salir):
	
	
	if  ((numero not in lista_fila[fila]) and (numero not in lista_columna[columna])) :
		if ((columna_a_num[columna] >= 1 and columna_a_num[columna] <=3 ) and
			( fila_cambio_a_numero[fila] >= 1 and fila_cambio_a_numero[fila] <= 3 )): 
			if not (numero in r1 ):
				# quitar el anterior
				lista_fila[fila].remove(asignacion[casilla])
				lista_columna[columna].remove(asignacion[casilla])
				r1.remove(asignacion[casilla])
				# insertar número que quieres
				lista_fila[fila].insert(1,numero)
				lista_columna[columna].insert(1,numero)
				r1.insert(1,numero)
				#
				asignacion[casilla]=numero
				
		elif ((columna_a_num[columna] >= 4 and columna_a_num[columna] <=6 ) and
			( fila_cambio_a_numero[fila] >= 1 and fila_cambio_a_numero[fila] <= 3 )): 
			if not (numero in r2 ):
				# quitar el anterior
				lista_fila[fila].remove(asignacion[casilla])
				lista_columna[columna].remove(asignacion[casilla])
				r2.remove(asignacion[casilla])
				# insertar número que quieres
				lista_fila[fila].insert(1,numero)
				lista_columna[columna].insert(1,numero)
				r2.insert(1,numero)
				asignacion[casilla]=numero
				
		elif ((columna_a_num[columna] >= 7 and columna_a_num[columna] <=9 ) and
			( fila_cambio_a_numero[fila] >= 1 and fila_cambio_a_numero[fila] <= 3 )): 
			if not (numero in r3 ):
				# quitar el anterior
				lista_fila[fila].remove(asignacion[casilla])
				lista_columna[columna].remove(asignacion[casilla])
				r3.remove(asignacion[casilla])
				# insertar número que quieres
				lista_fila[fila].insert(1,numero)
				lista_columna[columna].insert(1,numero)
				r3.insert(1,numero)
				asignacion[casilla]=numero
				
		elif ((columna_a_num[columna] >= 1 and columna_a_num[columna] <=3 ) and
			( fila_cambio_a_numero[fila] >= 4 and fila_cambio_a_numero[fila] <= 6 )): 
			if not (numero in r4 ):
				# quitar el anterior
				lista_fila[fila].remove(asignacion[casilla])
				lista_columna[columna].remove(asignacion[casilla])
				r4.remove(asignacion[casilla])
				# insertar número que quieres
				lista_fila[fila].insert(1,numero)
				lista_columna[columna].insert(1,numero)
				r4.insert(1,numero)
				asignacion[casilla]=numero
				
		elif ((columna_a_num[columna] >= 4 and columna_a_num[columna] <=6 ) and
			( fila_cambio_a_numero[fila] >= 4 and fila_cambio_a_numero[fila] <= 6 )): 
			if not (numero in r5 ):
				# quitar el anterior
				lista_fila[fila].remove(asignacion[casilla])
				lista_columna[columna].remove(asignacion[casilla])
				r5.remove(asignacion[casilla])
				# insertar número que quieres
				lista_fila[fila].insert(1,numero)
				lista_columna[columna].insert(1,numero)
				r5.insert(1,numero)
				asignacion[casilla]=numero
				
		elif ((columna_a_num[columna] >= 7 and columna_a_num[columna] <=9 ) and
			( fila_cambio_a_numero[fila] >= 4 and fila_cambio_a_numero[fila] <= 6 )): 
			if not (numero in r6 ):
				# quitar el anterior
				lista_fila[fila].remove(asignacion[casilla])
				lista_columna[columna].remove(asignacion[casilla])
				r6.remove(asignacion[casilla])
				# insertar número que quieres
				lista_fila[fila].insert(1,numero)
				lista_columna[columna].insert(1,numero)
				r6.insert(1,numero)
				asignacion[casilla]=numero
				
		elif ((columna_a_num[columna] >= 1 and columna_a_num[columna] <=3 ) and
			( fila_cambio_a_numero[fila] >= 7 and fila_cambio_a_numero[fila] <= 9 )): 
			if not (numero in r7 ):
				# quitar el anterior
				lista_fila[fila].remove(asignacion[casilla])
				lista_columna[columna].remove(asignacion[casilla])
				r7.remove(asignacion[casilla])
				# insertar número que quieres
				lista_fila[fila].insert(1,numero)
				lista_columna[columna].insert(1,numero)
				r7.insert(1,numero)
				asignacion[casilla]=numero
				
		elif ((columna_a_num[columna] >= 4 and columna_a_num[columna] <=6 ) and
			( fila_cambio_a_numero[fila] >= 7 and fila_cambio_a_numero[fila] <= 9 )): 
			if not (numero in r8 ):
				# quitar el anterior
				lista_fila[fila].remove(asignacion[casilla])
				lista_columna[columna].remove(asignacion[casilla])
				r8.remove(asignacion[casilla])
				# insertar número que quieres
				lista_fila[fila].insert(1,numero)
				lista_columna[columna].insert(1,numero)
				r8.insert(1,numero)
				asignacion[casilla]=numero
				
		elif ((columna_a_num[columna] >= 7 and columna_a_num[columna] <=9 ) and
			( fila_cambio_a_numero[fila] >= 7 and fila_cambio_a_numero[fila] <= 9 )): 
			if not (numero in r9 ):
				# quitar el anterior
				lista_fila[fila].remove(asignacion[casilla])
				lista_columna[columna].remove(asignacion[casilla])
				r9.remove(asignacion[casilla])
				# insertar número que quieres
				lista_fila[fila].insert(1,numero)
				lista_columna[columna].insert(1,numero)
				r9.insert(1,numero)
				asignacion[casilla]=numero
							
	else:
		os.system('clear')
		print "Ese número ya existe en una linea o recuadro \nNo puede colocarse ahí"
		sleep (4)
	
	return lista_columna,lista_fila,fila_cambio_a_numero,columna_a_num,asignacion,salir 



#################################
#################################
#################################
################################
##############   pantalla de sudoku inicial ########

def sudoku(asignacion ):

	print ""
	print "    1   2   3   4   5   6   7   8   9"
	print "\033[;31m"+"  ______________________________________"+"\033[0;m"
	print "A||",asignacion['a1'],"|",asignacion['a2'],"|",asignacion['a3'],"\033[;31m"+":"+"\033[0;m",asignacion['a4'],"|",asignacion['a5'],"|",asignacion['a6'],"\033[;31m"+":"+"\033[0;m",asignacion['a7'],"|",asignacion['a8'],"|",asignacion['a9'],"||"
	print "  -------------------------------------"
	print "B||",asignacion['b1'],"|",asignacion['b2'],"|",asignacion['b3'],"\033[;31m"+":"+"\033[0;m",asignacion['b4'],"|",asignacion['b5'],"|",asignacion['b6'],"\033[;31m"+":"+"\033[0;m",asignacion['b7'],"|",asignacion['b8'],"|",asignacion['b9'],"||"
	print "  -------------------------------------"
	print "C||",asignacion['c1'],"|",asignacion['c2'],"|",asignacion['c3'],"\033[;31m"+":"+"\033[0;m",asignacion['c4'],"|",asignacion['c5'],"|",asignacion['c6'],"\033[;31m"+":"+"\033[0;m",asignacion['c7'],"|",asignacion['c8'],"|",asignacion['c9'],"||"
	print "\033[;31m"+"  ======================================"+"\033[0;m"
	print "D||",asignacion['d1'],"|",asignacion['d2'],"|",asignacion['d3'],"\033[;31m"+":"+"\033[0;m",asignacion['d4'],"|",asignacion['d5'],"|",asignacion['d6'],"\033[;31m"+":"+"\033[0;m",asignacion['d7'],"|",asignacion['d8'],"|",asignacion['d9'],"||"
	print "  -------------------------------------"
	print "E||",asignacion['e1'],"|",asignacion['e2'],"|",asignacion['e3'],"\033[;31m"+":"+"\033[0;m",asignacion['e4'],"|",asignacion['e5'],"|",asignacion['e6'],"\033[;31m"+":"+"\033[0;m",asignacion['e7'],"|",asignacion['e8'],"|",asignacion['e9'],"||"
	print "  -------------------------------------"
	print "F||",asignacion['f1'],"|",asignacion['f2'],"|",asignacion['f3'],"\033[;31m"+":"+"\033[0;m",asignacion['f4'],"|",asignacion['f5'],"|",asignacion['f6'],"\033[;31m"+":"+"\033[0;m",asignacion['f7'],"|",asignacion['f8'],"|",asignacion['f9'],"||"
	print "\033[;31m"+"  ======================================"+"\033[0;m"
	print "G||",asignacion['g1'],"|",asignacion['g2'],"|",asignacion['g3'],"\033[;31m"+":"+"\033[0;m",asignacion['g4'],"|",asignacion['g5'],"|",asignacion['g6'],"\033[;31m"+":"+"\033[0;m",asignacion['g7'],"|",asignacion['g8'],"|",asignacion['g9'],"||"
	print "  -------------------------------------"
	print "H||",asignacion['h1'],"|",asignacion['h2'],"|",asignacion['h3'],"\033[;31m"+":"+"\033[0;m",asignacion['h4'],"|",asignacion['h5'],"|",asignacion['h6'],"\033[;31m"+":"+"\033[0;m",asignacion['h7'],"|",asignacion['h8'],"|",asignacion['h9'],"||"
	print "  -------------------------------------"
	print "I||",asignacion['i1'],"|",asignacion['i2'],"|",asignacion['i3'],"\033[;31m"+":"+"\033[0;m",asignacion['i4'],"|",asignacion['i5'],"|",asignacion['i6'],"\033[;31m"+":"+"\033[0;m",asignacion['i7'],"|",asignacion['i8'],"|",asignacion['i9'],"||"
	print "\033[;31m"+"  ______________________________________"+"\033[0;m"
	print ""
	return asignacion


#################################
def condicion_entrada(fila,numero,columna,fila_cambio_a_numero,columna_a_num):

	if not ((fila in fila_cambio_a_numero ) and
			(columna in columna_a_num )):
		entrada= False
	
	else:
		if ((fila_cambio_a_numero[fila] >= 1 and fila_cambio_a_numero[fila] <=9 ) and
			(columna_a_num[columna] >= 1 and columna_a_num[columna] <= 9 ) and
			(numero >= 1 and numero <= 9 )):

			entrada=True
		else:
			entrada=False

	return entrada
###################################3

def falla_casilla(fila,columna,fila_cambio_a_numero,columna_a_num):	
	
	if not((fila_cambio_a_numero[fila] >= 1 and fila_cambio_a_numero[fila] <=9 ) and
		(columna_a_num[columna] >= 1 and columna_a_num[columna] <= 9 ) ):

	   fallo=True
	else:
		fallo=False
	return fallo
   
###################################3

def si_completas(A,B,C,D,E,F,G,H,I,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9):
	# ordena las listas
	listas={1:A,2:B,3:C,4:D,5:E,6:F,7:G,8:H,9:I,10:l1,11:l2,12:l3,13:l4,14:l5,15:l6,16:l7,17:l8,18:l9,19:r1,20:r2,21:r3,22:r4,23:r5,24:r6,25:r7,26:r8,27:r9}
	for x in xrange(1,28):
		listas[x].sort()

	# condicion de salida
	plantilla=[1,2,3,4,5,6,7,8,9]
	# si todas las listas estan iguales a la plantilla ganas.
	if (( plantilla == A ) and ( plantilla == B ) and ( plantilla == C ) and ( plantilla == D ) and( plantilla == E ) and( plantilla == F ) and( plantilla == G ) and( plantilla == H ) and( plantilla == I ) and( plantilla == l1 ) and( plantilla == l2 ) and( plantilla == l3 ) and( plantilla == l4 ) and( plantilla == l5 ) and( plantilla == l6 ) and( plantilla == l7 ) and( plantilla == l8 ) and( plantilla == l9 ) and( plantilla == r1 ) and( plantilla == r2 ) and( plantilla == r3 ) and( plantilla == r4 ) and( plantilla == r5 ) and( plantilla == r6 ) and( plantilla == r7 ) and( plantilla == r8 ) and( plantilla == r9 )):
		return True
	else:
		return False

###################################3
###################################3
###################################3
###################################3
##
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

###################################3
###################################3
salir = False
numero=0
fila=20
columna=20


# condiciones de entrada
salir,numero,fila,columna,casilla = condiciones_de_entrada(salir,numero,fila,columna,si_completas,sudoku,condicion_entrada,fila_cambio_a_numero,columna_a_num,asignacion)

##
salir = False
while salir == False:
	# asignaciones añade el numero a las filas y casilla
	lista_columna,lista_fila,fila_cambio_a_numero,columna_a_num,asignacion,salir = asignaciones(numero,fila,columna,casilla,lista_columna,lista_fila,fila_cambio_a_numero,columna_a_num,asignacion,salir)

	salir,numero,fila,columna,casilla = condiciones_de_entrada(salir,numero,fila,columna,si_completas,sudoku,condicion_entrada,fila_cambio_a_numero,columna_a_num,asignacion)
	

