# !/usr/bin/python
# -*-coding: utf-8-*-
##############################################
#          Llegim la taula "pedidos"         #
##############################################

import os
import sys
import string
import psycopg2    # CAl fer "dnf -y install python-psycopg2"


##############################################
#          Ens connectem a la BBDD           #
##############################################
try:
	conn = psycopg2.connect(database="training", user="postgres", password="jupiter")
	print "DATABASE OPENED SUCCESSFULLY \n"
	
except:
	print "CONNECTION ERROR"
	exit(2)



##############################################
#            Declarem el cursor              #
##############################################
cur = conn.cursor()

os.system('clear')
sortir = False

##############################################
#              Menu principal                #
##############################################
while sortir == False:	
	
	os.system('clear')
	print "OPCIONS \n 1- Llegir taula pedidos: \n 0- Sortir \n"

	opcio = raw_input('Escull una opció [0-1]: ')
	
    # Comprovem si l'opció és correcta
	if not opcio.isdigit() or not ( int(opcio) >= 0 and int(opcio) <= 1 ):
		os.system('clear')
		print "Opció incorrecta, torna a provar \n"
		tecla = raw_input('Prem una tecla per continuar')

	else:
		opcio = int(opcio)

    # Sortim
	if opcio == 0:
		print "Adeu! \n"
		sortir = True

	# Llegim la taula "pedidos"
	elif opcio == 1: 
		
		try:

########## crea una tabla
			
			with open('tabla.csv', 'w') as f:
				tabla = raw_input("Que tabla quieres ver? ")
				colu = raw_input("Que columnas quieres ver? ")
				where = raw_input("Quieres filtrar con where, order by, cualquier atributo postgre? \nSi no, pulsa enter: ") 	
				sql = '(Select '+colu+' from '+tabla+ ' ' +where+ ' )'
###########cur.copy_expert() introduce los datos en la tabla 				
				cur.copy_expert("copy "+sql+" to stdout with csv header", f)

			os.system('clear')

############# Su puta madre lo que ha costado lanzar el comando te encuadra perfecta una tabla exportada ############
############# 	cat tabla.csv | coumn -t -s ',' #######################

			from subprocess import Popen, PIPE

			p1 = Popen(["cat","tabla.csv"], stdout=PIPE)
			p2 = Popen(["column", "-t","-s','"], stdin=p1.stdout, stdout = PIPE)
			p1.stdout.close()
			result = ( p2.communicate()[0] )
			p1.wait

			print result

######################################################
				
			tecla = raw_input('Prem una tecla per continuar')

		
		except psycopg2.Error as er :
			print "-------- ERROR:", er.pgcode, " -------- \n"
			conn.rollback()

##############################################
#        Ens desconnectem de la BBDD         #
##############################################
conn.close()
