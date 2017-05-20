#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

def mi_rango(inicio,fin,incremento):
	while inicio <= fin :
		yield inicio
		
		inicio=inicio+incremento

octeto3=0
#host_utiles=65024
host_utiles=65534

if host_utiles > 254 :

	while host_utiles > 254:
		host_utiles = host_utiles - 255
		octeto3=octeto3+1
		
print octeto3,host_utiles

octeto4=5
ip=[192,168,10,5]
for x in range(1,11):
     print '{0:2}   {1:11}{2:3}'.format(x, ip[:3], octeto4)

masc_final=[255,255,255,0]
var=3
tabla=[]
for fila in mi_rango(0,0,1):
	print '{0:3}  '.format(fila),
	for col in mi_rango(1,5,1):
	
		if var == 3:					
			if col == 1:
				print '{0:3}.{1:3}.{2:3}.{3:3}   '.format(ip[0],ip[1],ip[2],octeto4),
			elif col ==2:
				print '{0:3}.{1:3}.{2:3}.{3:3}   '.format(ip[0],ip[1],ip[2],octeto4+1),
			elif col ==3:
				print '{0:3}.{1:3}.{2:3}.{3:3}   '.format(ip[0],ip[1],ip[2],octeto4+host_utiles),
			elif col ==4:
				print '{0:3}.{1:3}.{2:3}.{3:3}   '.format(ip[0],ip[1],ip[2],octeto4+host_utiles+1),
				octeto4 = octeto4+host_utiles+2
			elif col ==5:
				print '{0:3}.{1:3}.{2:3}.{3:3}'.format(masc_final[0],masc_final[1],masc_final[2],masc_final[3],),
				
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
