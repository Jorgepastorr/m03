#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import os
os.system('clear')
partidas = input("Cuantas partidas quieres jugar: ")

# cont cuenta numero partidas se resetea cada ronda , ronda --> rondas
ronda,cont=1,1

#  contp suma las partidas cada vez que empatan
# j1,j2,emp suman jugadas ganadao o empates
j1,j2,emp,contp=0,0,0,0

salir= False
while salir == False:

	# numero aleatorio del 1 al 100
	num= random.randint(1,100)
	print num,
	
	if num%7==0 or num%7==1:
		pl1 = "ti"
	
	elif num%7==2 or num%7==3 or num%7==6:
		pl1 = "pi"
		
	elif num%7==4 or num%7==5:
		pl1 = "pa"
		
	if num%5==0 or num%5==1 or num%5==2:
		pl2 = "pa"
		
	elif num%5==3 :
		pl2 = "ti"
		
	elif num%5==4 :
		pl2 = "pi"
		
	if ( pl1 == pl2 ):
		print "player 1",pl1,"y player 2",pl2," ''Empate'' "
		emp=emp+1
	elif ( pl1 == "pi" and pl2 == "ti" ) or ( pl1 == "pa" and pl2 == "pi" ) or   ( pl1 == "ti" and pl2 == "pa" ):
		print "player 1",pl1,"y player 2",pl2,"''Gana",pl1,"player 1''"
		j1=j1+1
	else:
		print "player 1",pl1,"y player 2",pl2,"''Gana",pl2,"player 2''"
		j2=j2+1
		
	if cont == partidas and j1 == j2 :
		print ""
		print ("\033[;31m"+"Empate vuelta a empezar"+'\033[0;m')
		print "player 1:",j1,"victorias"
		print "player 2:",j2,"victorias"
		print emp,"empates"
		print ""
# cada vez que emparan se resetea contadores y se suman el número de partidas a contp
		contp=cont+contp
		j1,j2,emp,cont=0,0,0,0
		ronda=ronda+1
		
	elif cont == partidas :
		salir = True
		cont = cont-1
		
	cont = cont+1

# crea la media de partidas ganadas en el ultimo turno
if j1 > j2 :
	media = ( j1 * 100 ) / partidas 
else:
	media = ( j2 * 100 ) / partidas

# crea el total de partidas
totalp=cont+contp

print "",partidas
print "\033[;34m""¡¡Ganador!!""\033[0;m"
print "media de:",media,"%"
print "player 1:",j1,"victorias"
print "player 2:",j2,"victorias"
print emp,"empates"
print totalp,"partidas"
print "Total de rondas:",ronda
