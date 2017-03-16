#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Realizar  un  algoritmo  que  permita  leer  dos  valores. 
#Determinamos  cual  de  los  dos  valores  es  el mayor y lo mostramos por pantalla.
#Si son iguales lo decimos también.

import os
os.system('clear')

num1 = raw_input("Primer número: ")
num2 = raw_input("Segundo número: ")

if num1 > num2:
	print num1+" es mayor que "+num2
elif num1 == num2:
	print num1+" y "+num2+" son iguales"
else:
	print num2+" es mayor que "+num1
	  
