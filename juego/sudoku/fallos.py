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
A,B,C,D,E,F,G,H,I=[0],[],[],[],[],[],[],[],[]
l1,l2,l3,l4,l5,l6,l7,l8,l9=[0],[0],[],[],[],[],[],[],[]
r1,r2,r3,r4,r5,r6,r7,r8,r9=[0],[],[],[],[],[],[],[],[]

#################################

#### variables del panel
a1,a2,a3,a4,a5,a6,a7,a8,a9=0,0,0,0,0,0,0,0,0
b1,b2,b3,b4,b5,b6,b7,b8,b9=0,0,0,0,0,0,0,0,0
c1,c2,c3,c4,c5,c6,c7,c8,c9=0,0,0,0,0,0,0,0,0
d1,d2,d3,d4,d5,d6,d7,d8,d9=0,0,0,0,0,0,0,0,0
e1,e2,e3,e4,e5,e6,e7,e8,e9=0,0,0,0,0,0,0,0,0
f1,f2,f3,f4,f5,f6,f7,f8,f9=0,0,0,0,0,0,0,0,0
g1,g2,g3,g4,g5,g6,g7,g8,g9=0,0,0,0,0,0,0,0,0
h1,h2,h3,h4,h5,h6,h7,h8,h9=0,0,0,0,0,0,0,0,0
i1,i2,i3,i4,i5,i6,i7,i8,i9=0,0,0,0,0,0,0,0,0
#################################

#################################
#  niveles def
#################################

def asignacion_de_posicion(salir,A,B,C,D,E,F,G,H,I,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,numero,a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9):
	if casilla == "a1":				
		if (not numero in A) and (not numero in l1) and (not numero in r1):
			# quitar el anterior
			A.remove(a1)
			l1.remove(a1)
			r1.remove(a1)
			# insertar número que quieres
			A.insert(0,numero)
			l1.insert(0,numero)
			r1.insert(0,numero)
			a1=numero
			salir=True
		else:
			os.system('clear')
			print "Ese número ya existe en una linea o recuadro \nNo puede colocarse ahí"
			salir=True
			sleep (4)

	elif casilla == "a2":				
		if (not numero in A) and (not numero in l2) and (not numero in r1):
			# quitar el anterior
			A.remove(a2)
			l2.remove(a2)
			r1.remove(a2)
			# insertar número que quieres
			A.insert(1,numero)
			l2.insert(1,numero)
			r1.insert(1,numero)
			a2=numero
			salir=True
		else:
			os.system('clear')
			print "Ese número ya existe en una linea o recuadro \nNo puede colocarse ahí"
			salir=True
			sleep (4)
	elif casilla == "a3":				
		if (not numero in A) and (not numero in l3) and (not numero in r1):
			# quitar el anterior
			A.remove(a3)
			l3.remove(a3)
			r1.remove(a3)
			# insertar número que quieres
			A.insert(1,numero)
			l3.insert(1,numero)
			r1.insert(1,numero)
			a3=numero
			salir=True
		else:
			os.system('clear')
			print "Ese número ya existe en una linea o recuadro \nNo puede colocarse ahí"
			salir=True
			sleep (4)
	elif casilla == "a4":				
		if (not numero in A) and (not numero in l4) and (not numero in r2):
			# quitar el anterior
			A.remove(a4)
			l4.remove(a4)
			r2.remove(a4)
			# insertar número que quieres
			A.insert(1,numero)
			l4.insert(1,numero)
			r2.insert(1,numero)
			a4=numero
			salir=True
		else:
			os.system('clear')
			print "Ese número ya existe en una linea o recuadro \nNo puede colocarse ahí"
			salir=True
			sleep (4)
	elif casilla == "a5":				
		if (not numero in A) and (not numero in l5) and (not numero in r2):
			# quitar el anterior
			A.remove(a5)
			l5.remove(a5)
			r2.remove(a5)
			# insertar número que quieres
			A.insert(1,numero)
			l5.insert(1,numero)
			r2.insert(1,numero)
			a5=numero
			salir=True
		else:
			os.system('clear')
			print "Ese número ya existe en una linea o recuadro \nNo puede colocarse ahí"
			salir=True
			sleep (4)
	elif casilla == "a6":				
		if (not numero in A) and (not numero in l6) and (not numero in r2):
			# quitar el anterior
			A.remove(a6)
			l6.remove(a6)
			r2.remove(a)
			# insertar número que quieres
			A.insert(1,numero)
			l6.insert(1,numero)
			r2.insert(1,numero)
			a6=numero
			salir=True
		else:
			os.system('clear')
			print "Ese número ya existe en una linea o recuadro \nNo puede colocarse ahí"
			salir=True
			sleep (4)
	elif casilla == "a7":				
		if (not numero in A) and (not numero in l7) and (not numero in r3):
			# quitar el anterior
			A.remove(a7)
			l7.remove(a7)
			r3.remove(a7)
			# insertar número que quieres
			A.insert(1,numero)
			l7.insert(1,numero)
			r3.insert(1,numero)
			a7=numero
			salir=True
		else:
			os.system('clear')
			print "Ese número ya existe en una linea o recuadro \nNo puede colocarse ahí"
			salir=True
			sleep (4)
	elif casilla == "a8":				
		if (not numero in A) and (not numero in l8) and (not numero in r3):
			# quitar el anterior
			A.remove(a8)
			l8.remove(a8)
			r3.remove(a8)
			# insertar número que quieres
			A.insert(1,numero)
			l8.insert(1,numero)
			r3.insert(1,numero)
			a8=numero
			salir=True
		else:
			os.system('clear')
			print "Ese número ya existe en una linea o recuadro \nNo puede colocarse ahí"
			salir=True
			sleep (4)
	elif casilla == "a9":				
		if (not numero in A) and (not numero in l9) and (not numero in r3):
			# quitar el anterior
			A.remove(a9)
			l9.remove(a9)
			r3.remove(a9)
			# insertar número que quieres
			A.insert(1,numero)
			l9.insert(1,numero)
			r3.insert(1,numero)
			a9=numero
			salir=True
		else:
			os.system('clear')
			print "Ese número ya existe en una linea o recuadro \nNo puede colocarse ahí"
			salir=True
			sleep (4)

	return salir,A,B,C,D,E,F,G,H,I,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,numero,a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9
################################
def sudoku(a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9):

	print ""
	print "    1   2   3   4   5   6   7   8   9"
	print "\033[;31m"+"  ______________________________________"+"\033[0;m"
	print "A||",a1,"|",a2,"|",a3,"\033[;31m"+":"+"\033[0;m",a4,"|",a5,"|",a6,"\033[;31m"+":"+"\033[0;m",a7,"|",a8,"|",a9,"||"
	print "  -------------------------------------"
	print "B||",b1,"|",b2,"|",b3,"\033[;31m"+":"+"\033[0;m",b4,"|",b5,"|",b6,"\033[;31m"+":"+"\033[0;m",b7,"|",b8,"|",b9,"||"
	print "  -------------------------------------"
	print "C||",c1,"|",c2,"|",c3,"\033[;31m"+":"+"\033[0;m",c4,"|",c5,"|",c6,"\033[;31m"+":"+"\033[0;m",c7,"|",c8,"|",c9,"||"
	print "\033[;31m"+"  ======================================"+"\033[0;m"
	print "D||",d1,"|",d2,"|",d3,"\033[;31m"+":"+"\033[0;m",d4,"|",d5,"|",d6,"\033[;31m"+":"+"\033[0;m",d7,"|",d8,"|",d9,"||"
	print "  -------------------------------------"
	print "E||",e1,"|",e2,"|",e3,"\033[;31m"+":"+"\033[0;m",e4,"|",e5,"|",e6,"\033[;31m"+":"+"\033[0;m",e7,"|",e8,"|",e9,"||"
	print "  -------------------------------------"
	print "F||",f1,"|",f2,"|",f3,"\033[;31m"+":"+"\033[0;m",f4,"|",f5,"|",f6,"\033[;31m"+":"+"\033[0;m",f7,"|",f8,"|",f9,"||"
	print "\033[;31m"+"  ======================================"+"\033[0;m"
	print "G||",g1,"|",g2,"|",g3,"\033[;31m"+":"+"\033[0;m",g4,"|",g5,"|",g6,"\033[;31m"+":"+"\033[0;m",g7,"|",g8,"|",g9,"||"
	print "  -------------------------------------"
	print "H||",h1,"|",h2,"|",h3,"\033[;31m"+":"+"\033[0;m",h4,"|",h5,"|",h6,"\033[;31m"+":"+"\033[0;m",h7,"|",h8,"|",h9,"||"
	print "  -------------------------------------"
	print "I||",i1,"|",i2,"|",i3,"\033[;31m"+":"+"\033[0;m",i4,"|",i5,"|",i6,"\033[;31m"+":"+"\033[0;m",i7,"|",i8,"|",i9,"||"
	print "\033[;31m"+"  ______________________________________"+"\033[0;m"
	print ""
	return a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9



#################################
def condicion_entrada(casilla,numero):
	if (((casilla == "a1") or (casilla == "a2") or (casilla == "a3") or (casilla == "a4") or (casilla == "a5") or (casilla == "a6") or (casilla == "a7") or (casilla == "a8") or (casilla == "a9") or
		(casilla == "b1") or (casilla == "b2") or (casilla == "b3") or (casilla == "b4") or (casilla == "b5") or (casilla == "b6") or (casilla == "b7") or (casilla == "b8") or (casilla == "b9") or
		(casilla == "c1") or (casilla == "c2") or (casilla == "c3") or (casilla == "c4") or (casilla == "c5") or (casilla == "c6") or (casilla == "c7") or (casilla == "c8") or (casilla == "c9") or
		(casilla == "d1") or (casilla == "d2") or (casilla == "d3") or (casilla == "d4") or (casilla == "d5") or (casilla == "d6") or (casilla == "d7") or (casilla == "d8") or (casilla == "d9") or
		(casilla == "e1") or (casilla == "e2") or (casilla == "e3") or (casilla == "e4") or (casilla == "e5") or (casilla == "e6") or (casilla == "e7") or (casilla == "e8") or (casilla == "e9") or
		(casilla == "f1") or (casilla == "f2") or (casilla == "f3") or (casilla == "f4") or (casilla == "f5") or (casilla == "f6") or (casilla == "f7") or (casilla == "f8") or (casilla == "f9") or
		(casilla == "g1") or (casilla == "g2") or (casilla == "g3") or (casilla == "g4") or (casilla == "g5") or (casilla == "g6") or (casilla == "g7") or (casilla == "g8") or (casilla == "g9") or
		(casilla == "h1") or (casilla == "h2") or (casilla == "h3") or (casilla == "h4") or (casilla == "h5") or (casilla == "h6") or (casilla == "h7") or (casilla == "h8") or (casilla == "h9") or
		(casilla == "i1") or (casilla == "i2") or (casilla == "i3") or (casilla == "i4") or (casilla == "i5") or (casilla == "i6") or (casilla == "i7") or (casilla == "i8") or (casilla == "i9") )
		 and (numero >= 1 and numero <= 9 )):
		
		entrada=True
	else:
		entrada=False
	return entrada
###################################3

def falla_casilla(casilla):	
	if not( (casilla == "a1") or (casilla == "a2") or (casilla == "a3") or (casilla == "a4") or (casilla == "a5") or (casilla == "a6") or (casilla == "a7") or (casilla == "a8") or (casilla == "a9") or
			(casilla == "b1") or (casilla == "b2") or (casilla == "b3") or (casilla == "b4") or (casilla == "b5") or (casilla == "b6") or (casilla == "b7") or (casilla == "b8") or (casilla == "b9") or
			(casilla == "c1") or (casilla == "c2") or (casilla == "c3") or (casilla == "c4") or (casilla == "c5") or (casilla == "c6") or (casilla == "c7") or (casilla == "c8") or (casilla == "c9") or
			(casilla == "d1") or (casilla == "d2") or (casilla == "d3") or (casilla == "d4") or (casilla == "d5") or (casilla == "d6") or (casilla == "d7") or (casilla == "d8") or (casilla == "d9") or
			(casilla == "e1") or (casilla == "e2") or (casilla == "e3") or (casilla == "e4") or (casilla == "e5") or (casilla == "e6") or (casilla == "e7") or (casilla == "e8") or (casilla == "e9") or
			(casilla == "f1") or (casilla == "f2") or (casilla == "f3") or (casilla == "f4") or (casilla == "f5") or (casilla == "f6") or (casilla == "f7") or (casilla == "f8") or (casilla == "f9") or
			(casilla == "g1") or (casilla == "g2") or (casilla == "g3") or (casilla == "g4") or (casilla == "g5") or (casilla == "g6") or (casilla == "g7") or (casilla == "g8") or (casilla == "g9") or
			(casilla == "h1") or (casilla == "h2") or (casilla == "h3") or (casilla == "h4") or (casilla == "h5") or (casilla == "h6") or (casilla == "h7") or (casilla == "h8") or (casilla == "h9") or
			(casilla == "i1") or (casilla == "i2") or (casilla == "i3") or (casilla == "i4") or (casilla == "i5") or (casilla == "i6") or (casilla == "i7") or (casilla == "i8") or (casilla == "i9") 
		   ):
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

inicial = False
while inicial== False:
	
	os.system('clear')
	# plantilla def sudoku
	a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9=sudoku(a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9)
	print "salir: numero = -1"
	casilla = raw_input("casilla: ")
	numero = input("número: ") 

	salir = False
	while salir == False:
		
		# cuando todas las listas esten ordenadas del 1-9 ganas.
		if si_completas(A,B,C,D,E,F,G,H,I,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9):
			os.system('clear')
			print "¡¡ Felicidades !! Sin duda no tiene amigos."
			salir = True
			inicial= True
		## si quieres salir
		elif numero == -1:
			os.system('clear')
			print "Adios"
			salir = True
			inicial= True
	# si quieres jugar
		# condición para jugar (poner casilla y numero correcto)
		elif  condicion_entrada(casilla,numero):
			# def asignación de posición
			salir,A,B,C,D,E,F,G,H,I,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,numero,a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9 = asignacion_de_posicion(salir,A,B,C,D,E,F,G,H,I,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9,numero,a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9)
			###########################33
			

		######################333 en contrucción
#		#################333   asignacion_de_posicion
		else:
	# posibles fallos
			os.system('clear')
			if falla_casilla(casilla):
				print "Casilla incorrecta"
			if numero < 1 or numero > 9 :
				print "número erroneo"
			
			sleep (4)
			os.system('clear')
			# plantilla def sudoku
			a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9=sudoku(a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9)
			print "salir: numero = -1"
			casilla = raw_input("casilla: ")
			numero = input("número: ") 
