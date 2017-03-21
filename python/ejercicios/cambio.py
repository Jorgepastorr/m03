#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.system('clear')

precio = input("Inseta el precio del producto: ")
dinero = input("Cuanto pagas: ")
cambio= dinero - precio
b500=1
b200=1
b100=1
b50=1
b20=1
b10=1
b5=1
b2=1
b1=1
print "Cambio es",cambio

salir = False
while salir == False:

	if precio > dinero:
		print "Dinero insuficiente"
		salir= True
	elif cambio %500==0 and cambio >= 500:
		t500 = b500=b500+1
	elif cambio %200==0 and cambio < 500 and cambio >= 200:
		t200= b200=b200+1
	elif cambio %100==0 and cambio < 200 and cambio >= 100:
		t100= b100=b100+1
	elif cambio %50==0 and cambio < 100 and cambio >= 50:
		t50= b50=b50+1
	elif cambio %20==0 and cambio < 100 and cambio >= 20:
		t20= b20=b20+1
	elif cambio %10==0 and cambio < 20 and cambio >= 10:
		t10= b10=b10+1
	elif cambio %5==0 and cambio < 10 and cambio >= 5:
		t5= b5=b5+1
	elif cambio %2==0 and cambio < 5 and cambio >= 2:
		t2= b2=b2+1
	elif cambio %1==0 and cambio < 2 and cambio >= 1:
		t1= b1=b1+1
	elif cambio < 0:
		print "billetes de 500:",t500 
		print "billetes de 200:",t200
		print "billetes de 100:",t100
		print "billetes de 50:",t50
		print "billetes de 20:",t20
		print "billetes de 10:",t10
		print "billetes de 5:",t5
		print "monedas de 2:",t2
		print "monedas de 1:",t1
		salir= True
	
	cambio= cambio -1
