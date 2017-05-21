#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mi_rango(inicio,final,incremento):

	while inicio <= final :
		yield inicio
		inicio = inicio + incremento

#####################3

numero=input("inserte número a pasar a binario: ")

for vueltas in mi_rango(1,8,1) :

	if vueltas == 1:
		if numero%2==1:
			a="1"
	
		elif numero%2==0:
			a="0"

	else: 
		if numero/2%2==1 :
			a="1"+a
			
		elif numero/2%2==0 :
			a="0"+a
		
		numero= numero/2


int(float(a))
print a
