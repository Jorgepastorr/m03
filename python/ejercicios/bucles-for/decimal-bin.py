#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mi_rango(inicio,final,incremento):

	while inicio <= final :
		yield inicio
		inicio = inicio + incremento




numero=input("inserte número a pasar a binario: ")

for vueltas in mi_rango(1,7,1) :

		if numero//2%2==1 :
			print 1,
			numero= numero//2
			print numero
			
		if numero//2%2==0 :
			print 0,
			numero= numero//2
			print numero
