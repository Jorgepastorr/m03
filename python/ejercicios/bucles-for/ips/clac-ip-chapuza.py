#!/usr/bin/env python
# -*- coding: utf-8 -*-

################
def my_rango(inicio,fin,incremento):
	while inicio <= fin :
		yield inicio
		
		inicio=inicio+incremento

###################################################33
print "Separa los octetos por comas."
li=input("ip: ")

var=0
masbred=0
cont=1


salir =False
while salir == False:
	mascara=raw_input("mascara: b/c ")
	if mascara == "c":
		salir =True
	elif mascara == "b":
		redes=input("Cuantas redes quieres max 255: ")
		salir =True
	else:
		print "opción incorrecta"

if mascara == "c":
	for fila in my_rango(1,2,1):
		for col in my_rango(1,4,1):
			if fila == 1:
				if col == 1:
					print "       red        ",
				elif col ==2:
					print "    Primer host   ",
				elif col ==3:
					print "   Ultimo host    ",
				elif col ==4:
					print "     Brodcast      ",
					
			elif fila == 2:
				if col == 1:
					print li[:3],
					print var," ",
				elif col ==2:
					print li[:3],
					print var+1," ",
				elif col ==3:
					print li[:3],
					print var+254," ",
				elif col ==4:
					print li[:3],
					print var+255," ",
		print ""

elif mascara == "b":
	for fila in my_rango(1,redes,1):
		for col in my_rango(1,4,1):
			if fila == 1:
				if col == 1:
					print "       red        ",
				elif col ==2:
					print "    Primer host   ",
				elif col ==3:
					print "   Ultimo host    ",
				elif col ==4:
					print "     Brodcast      ",
					
			else :
				if col == 1:
					print cont,
					print li[:2],
					print masbred,var,"  ",
					
				elif col ==2:
					print li[:2],
					print masbred,var+1,"  ",
				elif col ==3:
					print li[:2],
					print masbred,var+254,"  ",
				elif col ==4:
					print li[:2],
					print masbred,var+255," ",
				
		masbred=masbred+1
		print ""
		cont=cont+1
		
