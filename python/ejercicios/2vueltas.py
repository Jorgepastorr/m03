#!/usr/bin/env python
# -*- coding: utf-8 -*-

print " "
vueltas= 0
num= 1
salir = False
while salir == False :

    if num%8==1 or num%8==2 :
        print " /\ "
    
    elif num%8==3 or num%8==4 :
        print " -->"
    
    elif num%8==5 or num%8==6 :
        print " \/ "
    
    elif num%8==7 or num%8==0 :
        print " <-- "
 
	if num == 8 :
		vueltas = vueltas+1
		num = 0
		print " "
	if vueltas == 2 :
		salir = True
    
    num=num+1
