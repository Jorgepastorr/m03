#!/usr/bin/env python
# -*- coding: utf-8 -*-
print 'opciones 1/2/3/4/5/6/7/8/9/10/J/Q/K/A' 
num=raw_input("mayor: ")
num2=raw_input("menor: ")

d = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14}



if d[num] > d[num2] :
	print 'cierto'
	print num," > ",num2
else:
	print 'Falso'
	print num," < ",num2

