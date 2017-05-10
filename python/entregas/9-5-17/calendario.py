#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mi_rango(inicio,final,incremento):
	
	if inicio <= final :
		while inicio <= final :
			yield inicio
			inicio = inicio + incremento
	else:
		while inicio >= final :
			yield inicio
			inicio = inicio - incremento
		
#############3
mes=raw_input("que mes quieres ver de este año? ")

cont = 1		
inicio_mes = {"enero":7,"febrero":3,"marzo":3,"abril":6,"mayo":1,"junio":4,"julio":6,"agosto":2,"septiembre":5,"octubre":7,"noviembre":3,"diciembre":5}
fin_mes =  {"enero":31,"febrero":28,"marzo":31,"abril":30,"mayo":31,"junio":30,"julio":31,"agosto":31,"septiembre":30,"octubre":31,"noviembre":30,"diciembre":31}

for fila in mi_rango(1,7,1):
	for columna in mi_rango(1,7,1):
		if (fila == 1 ):
			if columna == 1 :
				print "L ",
			if columna == 2 :
				print "M ",
			if columna == 3 :
				print "X ",
			if columna == 4 :
				print "J ",
			if columna == 5 :
				print "V ",
			if columna == 6 :
				print "S ",
			if columna == 7 :
				print "D ",
		
		elif ( fila == 2 ):
			if (inicio_mes[mes] <= columna ):
				print cont,"",
				cont=cont+1
			else:
				print "  ",
	
		elif ( cont <= fin_mes[mes] ):
			####### solo para que quede bonito.
			if cont < 10 :
				print cont,"",
				cont=cont+1
			#################
			else:
				print cont,
				cont=cont+1
	
		else: 
			print " ",
	
	print " "


#####################
