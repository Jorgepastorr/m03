#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.system('clear')

precio = input("Inseta el precio del producto: ")
dinero = input("Cuanto pagas: ")
cambio= dinero - precio
b500=0
b200=0
b100=0
b50=0
b20=0
b10=0
b5=0
b2=0
b1=0
print "Cambio es",cambio

salir = False
while salir == False:

	if precio > dinero:
		print "Dinero insuficiente"
		salir= True
	elif cambio >= 500:
		b500=b500+1
		cambio=cambio-499
	elif cambio < 500 and cambio >= 200:
		b200=b200+1
		cambio=cambio-199
	elif cambio < 200 and cambio >= 100:
		b100=b100+1
		cambio=cambio-99
	elif cambio < 100 and cambio >= 50:
		b50=b50+1
		cambio=cambio-49
	elif cambio < 100 and cambio >= 20:
		b20=b20+1
		cambio=cambio-19
	elif cambio < 20 and cambio >= 10:
		b10=b10+1
		cambio=cambio-9
	elif cambio < 10 and cambio >= 5:
		b5=b5+1
		cambio=cambio-4
	elif cambio < 5 and cambio >= 2:
		b2=b2+1
		cambio=cambio-1
	elif cambio < 2 and cambio >= 1:
		b1=b1+1
	elif cambio < 0:
		print "billetes de 500:",b500 
		print "billetes de 200:",b200
		print "billetes de 100:",b100
		print "billetes de 50:",b50
		print "billetes de 20:",b20
		print "billetes de 10:",b10
		print "billetes de 5:",b5
		print "monedas de 2:",b2
		print "monedas de 1:",b1
		salir= True
	
	cambio= cambio -1
