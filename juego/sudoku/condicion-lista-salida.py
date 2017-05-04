#!/usr/bin/env python
# -*- coding: utf-8 -*-

## listas de lineas y recuadros
A,B,C,D,E,F,G,H,I=[1,2,4,3],[5,8,7],[],[],[],[],[],[],[]
l1,l2,l3,l4,l5,l6,l7,l8,l9=[],[],[],[],[],[],[],[],[]
r1,r2,r3,r4,r5,r6,r7,r8,r9=[],[],[],[],[],[],[],[],[9,4,8,1]

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


# cuando todas las listas esten ordenadas del 1-9 ganas.
if si_completas(A,B,C,D,E,F,G,H,I,l1,l2,l3,l4,l5,l6,l7,l8,l9,r1,r2,r3,r4,r5,r6,r7,r8,r9):
	print "¡¡ Felicidades !! Sin duda no tiene amigos."
elif casilla == "-1":
	print "Hasta la próxima"
else:
	print "if condicion de entrada"



