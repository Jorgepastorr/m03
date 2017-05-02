#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.system('clear')
# llave sala3 abre puerta sala 2
llave = True

# explicación de juego y opciones
print '\033[;32m'+"""\nPasara por una serie de mazmorras, donde tendra una serie de retos.
Las funciones básicas seran: 
avanzar, retroceder o explorar salas y pasillos
abrir, cerrar o cojer los objetos del escenario.
\nPodra salir siemre que este en la sala principal y escriba salir.
'escribir siempre en minúsculas'"""+'\033[0;m'
print""

# sala 1
s1 = False
while s1 == False:
	print ""
	print "Esta en la sala principal"
	op1= raw_input("Que desa hacer: ")
	
	if ((op1 != "salir"				) and
	    (op1 != "explorar sala"		) and
	    (op1 != "explorar espejo"	) and
	    (op1 != "romper espejo"		) and
	    (op1 != "abrir puerta"		)):
		os.system('clear')
		print '\033[;31m'+"No es posible",op1+'\033[0;m'
	
	elif op1 == "salir":
		os.system('clear')
		print "Abandona la mazmorra" 
		s1 = True
	
	elif op1 == "explorar sala":
		os.system('clear')
		print '\033[;34m'+"Está en una sala cuadrada, a su izquierda hay un espejo, a su dercha una pared de piedra y de frente una puerta."+'\033[0;m'
	
	elif op1 == "explorar espejo":
		os.system('clear')
		print '\033[;34m'+"Un espejo roñoso donde se ve tu rostro de pardillo acojonado "+'\033[0;m'
	
	elif op1 == "romper espejo":
		os.system('clear')
		print '\033[;34m'"""Crashh \nel espejo se hace a ñicos y toto de ti se te clava en el dedo meñique del pie \n¡¡IDIOTA!!"""+'\033[0;m'
	
	elif op1 == "abrir puerta":
		os.system('clear')
		print '\033[;34m'+"""La puerta se abre \nPasas a la siguiente sala"""+'\033[0;m'
		########## sala2 #######################33
		s2 = False
		while s2 == False:
			
			print ""
			print "Esta en la sala 2"
			op2 = raw_input("Que desa hacer: ")
			
			if ((op2 != "retroceder sala"	) and
				(op2 != "explorar sala"		) and
				(op2 != "abrir puerta"	 	) and
				(op2 != "avanzar pasillo"	)):
				os.system('clear')
				print '\033[;31m'+"No es posible",op2+'\033[0;m'
			
			elif op2 == "retroceder sala":
				os.system('clear')
				print '\033[;34m'+"Accede a la sala anterior"+'\033[0;m' 
				s2 = True
			
			elif op2 == "explorar sala":
				os.system('clear')
				print '\033[;34m'+"Se encuentra en una sala donde a su derecha hay una puerta \na su izquierda una pared de piedra \nde frente un pasillo"+'\033[0;m'
			
			elif op2 == "avanzar pasillo":
				########################  sala 3
				os.system('clear')
				print '\033[;34m'+"abanza por el pasillo y encuentra sala 3"+'\033[0;m'
					
				s3 = False
				while s3 == False:
					
					print ""
					print "Esta en la sala 3"
					op3 = raw_input("Que desa hacer: ")
					
					if ((op3 != "retroceder sala"	) and
						(op3 != "explorar sala"		) and
						(op3 != "abrir cofre"	 	) and
						(op3 != "explorar cofre"	)):
						os.system('clear')
						print '\033[;31m'+"No es posible",op3+'\033[0;m'
					
					elif op3 == "retroceder sala":
						os.system('clear')
						print '\033[;34m'+"Accede a la sala anterior"+'\033[0;m' 
						s3 = True
					
					elif op3 == "explorar sala":
						os.system('clear')
						print '\033[;34m'+"Se encuentra en una sala redonda donde encuentra un cofre en estado putrefacto"+'\033[0;m'
					
					elif op3 == "abrir cofre":
						os.system('clear')
						print '\033[;34m'+"Encuentra una LLave"+'\033[0;m'
						op31 = raw_input("quiere recogerla? si/no ")
	#### llave de puerta sala 2 #############
						if op31 == "si":
							os.system('clear')
							llave = False
							print '\033[;34m'+"Recoge la llave"+'\033[0;m'
						
						elif op31 == "no":
							os.system('clear')
							print '\033[;34m'+"La llave se queda en el cofre"+'\033[0;m'
						
						elif (op31 != "si") and (op31 != "no"):
							print '\033[;31m'+"Los valores introducidos no son correctos"+'\033[0;m'
					
					elif op3 == "explorar cofre":
						os.system('clear')
						print '\033[;34m'+"Un cofre muy deteriorado, parece facil de abrir"+'\033[0;m'
				 ############ Fin sala 3

			####################################
			### sala2 puerta enlace con boss 1 redes #########
			elif op2 == "abrir puerta":
				os.system('clear')
				if llave == True:
					print '\033[;35m'+"La puerta esta cerrada"+'\033[0;m'
				
				else:
		#############  presala de Boss 1 tienes 3 oportunidades para derrotar el boss
					print '\033[;34m'+"¡¡premio pasaste el nivel!!\n"+'\033[0;m'
					
					rondasb1 = 3
					preboss = False
					while preboss == False:		
						
						if rondasb1 <= 0 :
							os.system('clear')
							print '\033[;31m'+"¡¡Te quedaste sin oportunidades!!"+'\033[0;m'
							s1 = True
							s2 = True
							preboss = True
						
						else:
							print '\033[;34m'+"Tienes",rondasb1,"oportunidades para derrotar al siguiente boss. \nSi elige no enfrentarte saldras del juego.\n"+'\033[0;m'
							opre = raw_input("Quieres enfrentarte:  si/no ")
								
							if opre == "no":	
								os.system('clear')
								print "pirate"
								s1 = True
								s2 = True
								preboss = True
							
							elif not((opre == "si") or
									 (opre == "no")
									):
								os.system('clear')
								print '\033[;31m'+"Esta opcion no está disponible\n"+'\033[0;m'
							
							elif opre == "si" :
								rondasb1 = rondasb1-1
								os.system('clear')
								print "juegas"
						
###################33######### fin de juego ###########






















