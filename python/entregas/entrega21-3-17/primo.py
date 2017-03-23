#!/usr/bin/env python
# -*- coding: utf-8 -*-

num = input("Introduce un número: ")
num2 = 2
salir = False
while salir == False :
	 
	if  num%num2==0 :
		print num,"no es primo"
		salir = True
	else :	
		print  num,"es primo"
		salir = True
	
	num2=num2+1
