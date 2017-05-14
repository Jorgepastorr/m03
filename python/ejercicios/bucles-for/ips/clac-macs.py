#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mi_rango(inicio,final,incremento):

	while inicio <= final :
		yield inicio
		inicio = inicio + incremento

#####################
#######################33

bits=input("Cuantos bits ocupa de red? Máximo 32 ")

unos=1
a= ""
li=[]

# da 32 vueltas número de bits totales de una mac
for fila in mi_rango(1,4,1) :
	for col in mi_rango(1,8,1) :
		# inserta 1 asta el número de bits elejidos
		if unos <= bits :
			a=a+"1"
		# cuando pasa de bits elegidos inserta 0
		else:
			a=a+"0"
		
		unos=unos+1
	
	# convierte números alfabeticos en numericos y lo inserta en lista (li)
	int(float(a))
	li.append(int(a))
	a=""
print li
######################## binario a decimal

resultado= 0
final= 0
mac=[]
var = 0
# da 4 vueltas 1 por octeto y 8 una por cada bit
for lista in mi_rango(1,4,1):
	for vuelta in mi_rango(0,7,1):
		if vuelta == 0:
			# diviode el num binario entre 10 si el resto da 1
			# suma 2^vuelta a final si no dfa 1 no tiene que suma nada
			if li[var]%10==1 :
				final = 2**vuelta
			resultado = li[var] // 10 
		
		else:
			if resultado%10==1 :
				final= final+2**vuelta
			resultado = resultado // 10 
	
	# añade el resultado de cada octeto en la lista mac
	mac.append(final)
	# suma 1 a var para cambiar de octeto
	var=var+1
	# resetea contadores para volver a sumar
	resultado= 0
	final= 0
	
print mac
