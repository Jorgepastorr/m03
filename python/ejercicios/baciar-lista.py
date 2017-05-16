#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

baraja=["A Picas","A Corazones","A Treboles","A Rombos","2 Picas","2 Corazones","2 Treboles","2 Rombos","3 Picas","3 Corazones","3 Treboles","3 Rombos","4 Picas","4 Corazones","4 Treboles","4 Rombos","5 Picas","5 Corazones","5 Treboles","5 Rombos","6 Picas","6 Corazones","6 Treboles","6 Rombos","7 Picas","7 Corazones","7 Treboles","7 Rombos","8 Picas","8 Corazones","8 Treboles","8 Rombos","9 Picas","9 Corazones","9 Treboles","9 Rombos","10 Picas","10 Corazones","10 Treboles","10 Rombos","J Picas","J Corazones","J Treboles","J Rombos","Q Picas","Q Corazones","Q Treboles","Q Rombos","K Picas","K Corazones","K Treboles","K Rombos"]

##################

var=51
#def carta_aleatoria(baraja,var):

salir = False
while salir == False:
	num = randint(0,var)		
	
	print baraja[num]
	baraja.remove(baraja[num])	
	var=var-1	
	##############
	
	print len(baraja)
	print var
	############3
		
	if len(baraja) == 0:
		print "Te quedaste sin cartas"
		salir = True
	#return baraja,num,var
