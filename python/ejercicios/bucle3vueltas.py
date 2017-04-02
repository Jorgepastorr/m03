#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


num= 1
vueltas= 0
salir= False

while salir == False :

    print num,

    if num%8==0 :
		vueltas= vueltas+1
		print " "
		num= 0
    if vueltas == 3 :
		salir = True
    
    num=num+1
