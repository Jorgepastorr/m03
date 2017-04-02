#!/usr/bin/env python
# -*- coding: utf-8 -*-
print "piedra, patel, tijera"
print "      pi/pa/ti"
pl1 = raw_input("player 1: ")
pl2 = raw_input("player 2: ")

if ( pl1 != pl2 ) :
	print "¡opciones incorrectas!"
	
elif ( pl1 == pl2 ):
	   print pl1,"y",pl2," Empate "

elif ( pl1 == "pi" and pl2 == "ti" ) or ( pl1 == "pa" and pl2 == "pi" ) or   ( pl1 == "ti" and pl2 == "pa" ):
		 print pl1,"y",pl2,"Gana",pl1,"player 1"
else:
	print pl1,"y",pl2,"Gana",pl2,"player 2"
