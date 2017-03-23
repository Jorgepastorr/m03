#!/usr/bin/env python
# -*- coding: utf-8 -*-
		
var = input("número ")
num1 = -1

a = 0
b = 1

salir = False
while salir == False:
		#a,b = b, a+b
		print  a,",",	
		x=a+b  
		a = b   
		b = x   
		
		if num1 == var :
			salir = True
		
		num1=num1+1
