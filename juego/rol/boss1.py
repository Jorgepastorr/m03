#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
import os
os.system("clear")

# explicacion de boss
print '\033[;32m'+"Te encuentras delante del Boss Redes \nTe está debilitando con su poder de esnifar ondas y tiene multiples cables de fibra con los que golperarte \nTendras que respinder a sus preguntas correctamente si quieres derrotarlo \nCon cada respuesta incorrecta te quita vida \n\nSi en alguna opción tiene varias respuestas: \nla sintaxis es x,x en orden alfabético"+'\033[0;m'

## lista de número de preguntas
lipreguntas=[]

####### vida =vida del jugador y count = vida del boss quien llega a 3 pierde.
count = 0
vida = 0
sb1 = False
while sb1 == False:
		####### numero aleatorio que escoje las preguntas introducidas en la lista
	num = randint(0,8)
	
	################# 1 mira el numero aleatorio, 2 un vez mostrado lo introduce en una lista, 3 solo sigue el script si el aleatorio no esta en la lista
	if len(lipreguntas) == 9: 						#### Si la lista tiene 6 numeros sale del boss (pierdes)
		print "Te quedaste sin preguntas ¡¡Pierdes!!"
		sb1 = True
	elif not num in lipreguntas : 					#### si el número aleatorio no esta en la lista puedes seguir
		lipreguntas.insert(1,num)					  #### añade el numero aleatorio a la lista
	#################
		
		#### preguntas del boss
		li=["""\nDonada l'adreça IP 172.50.0.0, necessitem 4 subxarxes. Quina serà la seva mascara ?\n\nTrieu-ne una:\na. 255.255.234.0\nb. 255.255.25.0\nc*. 255.255.224.0
			""","""
			\nQuina opció és certa pel que fa a les topologies física i lògica?\n\nTrieu-ne una:\na*.Les topologies lògiques consisteixen en connexions virtuals entre els nodes.\nb.Les topologies físiques s'ocupen de com una xarxa transmet les trames.\nc.La topologia lògica sempre és la mateixa que la topologia física.\nd.Els protocols de capa d'enllaç de dades defineixen les rutes de senyals físics.
			""","""
			\nQuina subcapa de la capa d'enllaç de dades prepara la senyal que es transmetrà per la capa física?\n\nTrieu-ne una:\na.LLC Incorrecte\nb.NIC\nc*.MAC\nd.HDLC
			""","""
			\nDonada una adreça IP 210.100.56.0 de classe C. Necessitem 6 subxarxes útils amb un mínim de 30 hosts cada una. Quina tindria de ser la seva mascara ?\n\nTrieu-ne una:\na*. 255.255.255.224 \nb. 255.255.255.124\nc. 255.255.255.232\nd. 255.255.255.32
			""","""
			\nDonada la IP 172.17.99.71 amb una mascara 255.255.0.0. Quin serà la direcció de broadcast per aquesta xarxa ?\n\nTrieu-ne una:\na. 172.255.255.255\nb. 172.17.0.0\nc*. 172.17.255.255\nd. 172.17.0.255\ne. 172.17.99.255
			""","""
			\nQuè determina el mètode de Control d'accés al medi (MAC)? (Tria dos).\n\nTrieu-ne una o més:\na*.l'ús compartit dels mitjans\nb.adreçament de la capa de xarxa \nc.processos de la capa d'aplicació\nd.funció dels dispositius intermediaris \ne*.topologia lògica
			""","""
			\nDonada la IP 223.69.230.250 amb la mascara 255.255.0.0 . Quin serà la adreça de xarxa la qual pertany aquesta IP ?\n\nTrieu-ne una:\na*. 223.69.0.0 \nb. 223.69.230.250\nc. 223.0.0.0\nd. 223.69.230.0
			""","""
			\nQuines opcions són propietats de l'accés als mitjans basat en la contenció per a mitjans compartits? (Tria tres).\n\nTrieu-ne una o més:\na.els dispositius han d'esperar el seu torn\nb*.menys despeses\nc.pas de tokens\nd*.existeixen col·lisions\ne.sempre transmet una estació alhora\nf*.no determinista 
			""","""
			\nQuins afirmacions són certes quan un dispositiu es trasllada d'una xarxa o subxarxa a una altra? (Tria dos).\n\nTrieu-ne una o més:\na.No s'ha de canviar l'adreça del gateway per defecte.\nb*.El dispositiu continuarà operant en la mateixa adreça de la Capa 2.\nc.S'haurà d'assignar nombres de ports addicionals a les aplicacions i serveis.\nd.S'ha de tornar a assignar l'adreça de la Capa 2. \ne*.S'ha de tornar a assignar l'adreça de la Capa 3 per permetre les comunicacions a la nova xarxa. Correcte
			"""
			]
		## muestra pregunta por pantalla
		print li[num]
		res= raw_input("Tu respuesta es: ")
		
		####### respuestas correctas segun su número en la lista
		if num == 0 and res == "c":
			count= count+1
			os.system("clear")
		elif num == 1 and res == "a":
			count= count+1
			os.system("clear")
		elif num == 2 and res == "c":
			count= count+1
			os.system("clear")
		elif num == 3 and res == "a":
			count= count+1
			os.system("clear")
		elif num == 4 and res == "c":
			count= count+1
			os.system("clear")
		elif num == 5 and (res == "a,e" or res == "e,a"):
			count= count+1
			os.system("clear")
		elif num == 6 and res == "a":
			count= count+1
			os.system("clear")
		elif num == 7 and res == "b,d,f" :
			count= count+1
			os.system("clear")
		elif num == 8 and (res == "b,e" or res == "e,b"):
			count= count+1
			os.system("clear")
		###### si la respuesta es incorrecta muestra error y te quita 1 e vida		
		if not((num == 0 and res == "c") or
			   (num == 1 and res == "a") or
			   (num == 2 and res == "c") or
			   (num == 3 and res == "a") or
			   (num == 4 and res == "c") or
			   (num == 5 and (res == "a,e" or res == "e,a")) or
			   (num == 6 and res == "a") or
			   (num == 7 and res == "b,d,f") or
			   (num == 8 and (res == "b,e" or res == "e,b"))
			  ):
			os.system("clear")
			print '\033[;35m'+"¡¡Respuesta incorrecta!! \nRedes se siente mas fuerte"+'\033[0;m'
			vida= vida+1
			count=count-1
		
			###### pasos de vida del jugador si llega a 3 pierdes
			if vida == 1:
				print "\033[;31m"+"Redes te golpea y te hiere"+'\033[0;m'
			elif vida == 2:
				print "\033[;31m"+"Redes te esnifa los pensamientos y te sientes debil"+'\033[0;m'
			elif vida == 3:
				os.system("clear")
				print '\033[;34m'+"¡¡Pierdes!! \nRedes te extrangula con un cable UTP-45 "+'\033[;31m'+"\nMueres asfixiado"+'\033[0;m'
				sb1 = True 
		
		#######pasos de vida del boss si llega a 3 ganas
		if count == 1 :
			print '\033[;31m'+"¡Redes está herido!"+'\033[0;m'
		elif count == 2 :
			print '\033[;31m'+"¡Redes está muy debil!"+'\033[0;m'
		elif count == 3 :
			print '\033[;34m'+"¡¡Ganaste!! \n¡¡Proximo nivel en construcción!!"+'\033[0;m'
			sb1 = True
	
