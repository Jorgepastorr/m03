#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import os
os.system("clear")

# black jack1

valor=0
valor_maquina=0
peticion=""

baraja=["A Picas","A Corazones","A Treboles","A Rombos",
"2 Picas","2 Corazones","2 Treboles","2 Rombos",
"3 Picas","3 Corazones","3 Treboles","3 Rombos",
"4 Picas","4 Corazones","4 Treboles","4 Rombos",
"5 Picas","5 Corazones","5 Treboles","5 Rombos",
"6 Picas","6 Corazones","6 Treboles","6 Rombos",
"7 Picas","7 Corazones","7 Treboles","7 Rombos",
"8 Picas","8 Corazones","8 Treboles","8 Rombos",
"9 Picas","9 Corazones","9 Treboles","9 Rombos",
"10 Picas","10 Corazones","10 Treboles","10 Rombos",
"J Picas","J Corazones","J Treboles","J Rombos",
"Q Picas","Q Corazones","Q Treboles","Q Rombos",
"K Picas","K Corazones","K Treboles","K Rombos"]

##################
def carta_aleatoria(baraja):
	maquina=""
	cartaj1=""

	# saca una aleatoria carta de la lista y la borra
	# para maquina
	if peticion == "planto":
		num = random.choice(baraja)	
		maquina = num
		baraja.remove(num)	
	
	# para j1	
	else:
		num = random.choice(baraja)		
		cartaj1 = num
		baraja.remove(num)	
		
	# núnca se cumplira no es posible quedarse sin cartas con solo 1 ronda	en el caso de que así fuera baraja de nuevo
	if len(baraja) == 0:
		print "Te quedaste sin cartas se vuelve a barajar"
		baraja=["A Picas","A Corazones","A Treboles","A Rombos","2 Picas","2 Corazones","2 Treboles","2 Rombos","3 Picas","3 Corazones","3 Treboles","3 Rombos","4 Picas","4 Corazones","4 Treboles","4 Rombos","5 Picas","5 Corazones","5 Treboles","5 Rombos","6 Picas","6 Corazones","6 Treboles","6 Rombos","7 Picas","7 Corazones","7 Treboles","7 Rombos","8 Picas","8 Corazones","8 Treboles","8 Rombos","9 Picas","9 Corazones","9 Treboles","9 Rombos","10 Picas","10 Corazones","10 Treboles","10 Rombos","J Picas","J Corazones","J Treboles","J Rombos","Q Picas","Q Corazones","Q Treboles","Q Rombos","K Picas","K Corazones","K Treboles","K Rombos"]

	return baraja,num,maquina,cartaj1
############################3

def asignacion_valores(cartaj1,valor):
	
	# asigna valores segun la carta
	if "A" in cartaj1:
		
		control_raw=False
		while control_raw == False:
			valorA= raw_input("Que valor quieres que tenga A: 1 o 11 ")	
			
			if valorA == "1" or valorA == "11":
				if valorA == "1" :
					valor= valor +1
				elif valorA == "11":
					valor= valor +11
				control_raw=True
				
			else:
				print "Esa opcion no es válida"
	
	elif "2" in cartaj1:
		valor= valor +2
	elif "3" in cartaj1:
		valor= valor +3
	elif "4" in cartaj1:
		valor= valor +4
	elif "5" in cartaj1:
		valor= valor +5
	elif "6" in cartaj1:
		valor= valor +6
	elif "7" in cartaj1:
		valor= valor +7
	elif "8" in cartaj1:
		valor= valor +8
	elif "9" in cartaj1:
		valor= valor +9
	elif "10" in cartaj1:
		valor= valor +10
	elif (("J" in cartaj1) or
		  ("Q" in cartaj1) or
		  ("K" in cartaj1)):
		valor= valor +10
	
	return valor

############################3
def asignacion_valores_maquina(maquina,valor_maquina):
	
	if "A" in maquina:
		valor_maquina = valor_maquina +1
	elif "2" in maquina:
		valor_maquina=valor_maquina+2
	elif "3" in maquina:
		valor_maquina=valor_maquina+3
	elif "4" in maquina:
		valor_maquina=valor_maquina+4
	elif "5" in maquina:
		valor_maquina=valor_maquina+5
	elif "6" in maquina:
		valor_maquina=valor_maquina+6
	elif "7" in maquina:
		valor_maquina=valor_maquina+7
	elif "8" in maquina:
		valor_maquina=valor_maquina+8
	elif "9" in maquina:
		valor_maquina=valor_maquina+9
	elif "10" in maquina:
		valor_maquina=valor_maquina+10
	elif (("J" in maquina) or
		  ("Q" in maquina) or
		  ("K" in maquina)):
		valor_maquina=valor_maquina+10
	
	return valor_maquina

###############################

def calculo_final(peticion,valor,baraja):
	
	# compara valores y calcula quien gana
	if peticion == "planto":
		#####
		valor_maquina=0
		while valor_maquina < 16 :
			# crea carta maquina
			baraja,num,maquina,cartaj1 = carta_aleatoria(baraja)
			# pone un valor
			valor_maquina = asignacion_valores_maquina(maquina,valor_maquina)
			
			# compara valores.
		os.system("clear")
		if valor <= valor_maquina :
			print "Pierdes J1:",valor," Máquina:",valor_maquina 
		
		elif valor > valor_maquina :
			print "Ganas J1:",valor," Máquina:",valor_maquina

	return peticion,valor 

################################



print "Black jack \nReglas del juego: \nTienes conseguir superar a la máquina con un máximo de 21"
print "A - 1 o 11 \nNúmeros equivale a su número \nJ,Q,K - 10\n"
print "Salir -1"
peticion=raw_input("Enter si quieres carta? ")	
os.system("clear")

salir = False
while salir == False:
	
	# condiciones de salida
	if (peticion == "-1") or (valor > 21 ) or (peticion == "planto"):
		salir = True
		print "¡¡ADIOS!!"
	else:
		# genera una carta aleatoria para j1
		baraja,num,maquina,cartaj1 = carta_aleatoria(baraja)
		print "\nTu carta es",cartaj1
		
		# asigna un valor segun la carta
		valor=asignacion_valores(cartaj1,valor)
		
		# si te has pasado de 21 pierdes
		if valor > 21 :
			print "Te pasaste gana la máquina"
			print valor
		# si es menor o igual a 21 puedes coger carta o plantarte
		else:
			print "Tienes",valor 
			print "Puedes plantate con 'planto'"
			print "Salir -1"
			peticion=raw_input("Enter si quieres carta? ")	
			os.system("clear")
           
           # si te plantas calcula carta y valor maquina y ve si ganas o pierdes
			peticion,valor = calculo_final(peticion,valor,baraja)









