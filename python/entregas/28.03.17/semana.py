#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
num = 1
salir = False
while salir == False :
    if num%7==1 :
        print "L tancat"
    
    elif num%7==2 :
        print "M"
    
    elif num%7==3 :
        print "X día espectacular"
    
    elif num%7==4 :
        print "J día espectacular"
    
    elif num%7==5 :
        print "V"
    
    elif num%7==6 :
        print "S sesio golfa"
    
    elif num%7==0 :
        print "D"
    
    if num == 7 :
        salir = True
    
    num=num+1
    
