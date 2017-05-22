#!/usr/bin/env python
# -*- coding: utf-8 -*-


#############  define un range 
def mi_rango(inicio,fin,incremento):
	while inicio <= fin :
		yield inicio
		
		inicio=inicio+incremento

#####################33
cont=0
numero=2048
while numero > 256:
	numero=numero-256
	cont=cont+1
	print numero
print cont,"",numero-1

	


#257
