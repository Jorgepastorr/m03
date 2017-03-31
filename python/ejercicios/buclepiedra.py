#!/usr/bin/env python
# -*- coding: utf-8 -*-

num= 31
salir= False
while salir == False:
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

	elif ( pl1 == "pi" and pl2 == "ti" ) or ( pl1 == "pa" and pl2 == "pi" ) or   ( pl1 == "ti" and pl2 == "pa" ):
			 print "player 1",pl1,"y player 2",pl2,"''Gana",pl1,"player 1''"
	else:
		print "player 1",pl1,"y player 2",pl2,"''Gana",pl2,"player 2''"

	if num == 57 :
		salir = True
	
	num = num+1
