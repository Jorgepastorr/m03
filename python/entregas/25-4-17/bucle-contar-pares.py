#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

######
# Bucle: Que cuente del número 1 hasta el límite que yo le diga. Sólo los pares.
# ejercicio-bucle-contar-pares.py
###########
var = input("num: ")
for i in range(1,var+1) :
	if i %2==0:
		print (i)
