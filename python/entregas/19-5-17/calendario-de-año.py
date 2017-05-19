#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar

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
anyo=input("Indica el año: ")

mes =1
cont = 1		
meses={1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}


for vuelta in mi_rango(1,12,1):
	# da la totalidad de días que tiene ese mes en ese año
	fin_dias_mes=calendar.monthrange(anyo, mes)[1]
	#~ da el día de la semana que empieza el mes de lunes a domingo en 1 - 7
	inicio_dia_semana=(calendar.weekday(anyo,mes,1))+1
	
	print meses[mes]
	
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
				if (inicio_dia_semana <= columna ):
					print cont,"",
					cont=cont+1
				else:
					print "  ",
		
			elif ( cont <= fin_dias_mes ):
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
	print ""
	mes=mes+1
	cont=1
	
#####################
