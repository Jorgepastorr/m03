#!/usr/bin/env python
# -*- coding: utf-8 -*-


#########
# Bucle: sumar desde el número 1 hasta el 5. Sólo los pares.
# Ha de salir por pantalla
# 2+4=9
# ejercicio-bucle-sumar.py
############
todo = 0
for i in range(1,6) :
	if i %2==0:
		print (i),
		todo = todo + 1

print "=",todo
