#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system('clear')

total = 0
anio = 1
salir = False
while salir == False:
		
		print anio,"+",
		total = anio + total
		if anio == 5:
			print "=",total
			salir = True

		anio = anio +1		
	
