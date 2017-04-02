#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system('clear')

var = input("Asta que numero queres que cuente? ")
anio = 1
salir = False
while salir == False:
		
		if anio > var:
			salir = True
		else:
			if anio %2==0:
				print anio
		anio = anio +1		
	
