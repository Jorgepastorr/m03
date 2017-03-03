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

########## cur.copy te muestra la tabla pero no se encuadrarla
			cur.copy_expert("copy pedidos to stdout with csv header", sys.stdout)

########## cur.execute() no funciona para exportar tablas da errores la \ ##########

#			cur.execute('\copy pedidos to /tmp/tablap.csv csv header ');
#			os.system('clear')

############# Su puta madre lo que ha costado lanzar el comando te encuadra perfecta una tabla exportada ############
############# 	cat /tmp/tablap.csv | coumn -t -s ',' #######################

#			from subprocess import Popen, PIPE

#			p1 = Popen(["cat","/tmp/tablap.csv"], stdout=PIPE)
#			p2 = Popen(["column", "-t","-s','"], stdin=p1.stdout, stdout = PIPE)
#			p1.stdout.close()
#			result = ( p2.communicate()[0] )
#			p1.wait

#			print result

######################################################
				
			tecla = raw_input('Prem una tecla per continuar')

		
		except psycopg2.Error as er :
			print "-------- ERROR:", er.pgcode, " -------- \n"
			conn.rollback()

##############################################
#        Ens desconnectem de la BBDD         #
##############################################
conn.close()
