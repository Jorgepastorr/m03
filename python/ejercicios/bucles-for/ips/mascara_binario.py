#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mi_rango(inicio,final,incremento):

	while inicio <= final :
		yield inicio
		inicio = inicio + incremento

#####################3
print "Separar octetos por comas ','"
mascara=input("inserte número de mascara a pasar a binario: ")
var = 0
mascara_binaria=[]
cont=0

for vueltas in mi_rango(1,4,1) :
	numero = mascara[var]
	for vueltas in mi_rango(1,8,1) :

		if vueltas == 1:
			if numero%2==1:
				a="1"
				cont=cont+1
			elif numero%2==0:
				a="0"

		else: 
			if numero/2%2==1 :
				a="1"+a
				cont=cont+1
			elif numero/2%2==0 :
				a="0"+a
			
			numero= numero/2
	var=var+1

	int(float(a))
	mascara_binaria.append(int(a))

print mascara_binaria
print cont
