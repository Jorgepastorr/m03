#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.system("clear")
dia =float( input("días: "))
ano=0
mes=0
semana=0
dias=0

salir = False
while salir == False:
	
	if dia >= 365 :
		ano= ano+1
		dia = dia-365
		
	elif dia >= 30 and dia < 365:
		mes=mes+1
		dia=dia-30.5
		
	elif dia >= 7 and dia < 30 :
		semana=semana+1
		dia=dia-7.5
		
	elif dia > 0 and dia < 7 :
		dias=dias+1
		dia = dia-1
		
	if dia  <= 0:
		salir = True 
	
print ""
print "años",ano
print "meses",mes
print "semanas",semana
print "dias",dias
