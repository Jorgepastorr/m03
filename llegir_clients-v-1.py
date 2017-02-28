# !/usr/bin/python
# -*-coding: utf-8-*-
##############################################
#          Llegim la taula "clientes"        #
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
	print "OPCIONS \n 6- Llegir taula 'repventas' \n 5- Llegir taula 'oficinas' \n 4- Llegir taula 'productos' \n 3- Llegir taula 'clientes' \n 2- Llegir taula 'pedidos' \n 1- bucle taulas \n 0- Sortir \n"
   
	opcio = raw_input('Escull una opció [0-1-2-3-4-5-6]: ')
	
    # Comprovem si l'opció és correcta
	if not opcio.isdigit() or not ( int(opcio) >= 0 and int(opcio) <= 6 ):
		os.system('clear')
		print "Opció incorrecta, torna a provar \n"
		tecla = raw_input('Prem una tecla per continuar')

	else:
		opcio = int(opcio)

    # Sortim
	if opcio == 0:
		print "Adeu! \n"
		sortir = True

###########################################
############ GUARREANDO BUcle dentro de opion 2 ############
# Llegim la taulas
	elif opcio == 1: 
		while sortir == False:	
	
			os.system('clear')
			print "Qué tabla quieres ver"
			print "1.-Pedidos"
			print "2.-Clientes"
			print "3.-Productos"
			print "4.-Oficinas"
			print "5.-Repventas"
			print "6.-Salir"
	
			opcio = raw_input('Escull una opció [0-1-2-3-4-5-6]: ')
			
			# Comprovem si l'opció és correcta
			if not opcio.isdigit() or not ( int(opcio) >= 0 and int(opcio) <= 6 ):
				os.system('clear')
				print "Opció incorrecta, torna a provar \n"
				tecla = raw_input('Prem una tecla per continuar')

			else:
				opcio = int(opcio)
			 # Sortim
			if opcio == 6:
				print "Adeu! \n"
				sortir = True
				
				
			
			# Llegim la taula "pedidos"
			elif opcio == 1: 
				
				try:			
						cur.execute("SELECT * FROM pedidos");
						rows = cur.fetchall()
						
						os.system('clear')
						
						print "NUM_PEDIDO FECHA_PEDIDO   CLIE     REP   FAB  PRODUCTO   CANT   IMPORTE "
						print "------------------------------------------------------------------------"
						
						for row in rows:
						   #print row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]
						   print(" {:^10} {} {:^10} {:^5} {:^5} {:^10} {:^5} {:^10} ".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
					
						tecla = raw_input('Prem una tecla per continuar')
				
				except psycopg2.Error as er :
					print "-------- ERROR:", er.pgcode, " -------- \n"
					conn.rollback()

############# Llegim la taula "clientes"
			elif opcio == 2: 
				
				try:	
								
						cur.execute("SELECT * FROM clientes");
						rows = cur.fetchall()
						
						os.system('clear')
						
						print "  num_clie        empresa        rep_clie   limite_credito  "
						print "------------------------------------------------------------"
						
						for row in rows:
						   #print row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]
						   print(" {:^10} {:^20} {:^10} {:^5} ".format(row[0], row[1], row[2], row[3]))
					
						tecla = raw_input('Prem una tecla per continuar')
				
				except psycopg2.Error as er :
					print "-------- ERROR:", er.pgcode, " -------- \n"
					conn.rollback()

		############## Productos			
			elif opcio == 3: 
				
				try:	
								
						cur.execute("SELECT * FROM productos");
						rows = cur.fetchall()
						
						os.system('clear')
						
						print " id_fab | id_producto |    descripcion    | precio  | existencias" 
						print " -------+-------------+-------------------+---------+-------------"

						
						for row in rows:
						   #print row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]
						   print(" {:^6} {:^13} {:^20} {:^10} {:^13} ".format(row[0], row[1], row[2], row[3], row[4]))
					
						tecla = raw_input('Prem una tecla per continuar')
				
				except psycopg2.Error as er :
					print "-------- ERROR:", er.pgcode, " -------- \n"
					conn.rollback()
					
		############### Oficinas
			elif opcio == 4: 
				
				try:	
								
						cur.execute("SELECT * FROM oficinas");
						rows = cur.fetchall()
						
						os.system('clear')
						
						print "  oficina |   ciudad    | region | dir | objetivo  |  ventas   "
						print " ---------+-------------+--------+-----+-----------+-----------"

						
						for row in rows:
						   #print row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]
						   print(" {:^8} {:^14} {:^8} {:^5} {:^11} {:^10} ".format(row[0], row[1], row[2], row[3], row[4], row[5]))
					
						tecla = raw_input('Prem una tecla per continuar')
				
				except psycopg2.Error as er :
					print "-------- ERROR:", er.pgcode, " -------- \n"
					conn.rollback()			
					
		################ Repventas
			elif opcio == 5: 
					
					try:	
									
							cur.execute("SELECT * FROM repventas");
							rows = cur.fetchall()
							
							os.system('clear')
							
							print " num_empl |    nombre     | edad | oficina_rep |   titulo   |  contrato  | director |   cuota   |  ventas   "
							print "----------+---------------+------+-------------+------------+------------+----------+-----------+-----------"

							
							for row in rows:
							   #print row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]
							   print(" {:^8} {:^17} {:^5} {:^14} {:^10}   {}   {:^8} {:^12} {:^12} ".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
						
							tecla = raw_input('Prem una tecla per continuar')
					
					except psycopg2.Error as er :
						print "-------- ERROR:", er.pgcode, " -------- \n"
						conn.rollback()			
	
################  FIN DE BUCLE   ##############
#############################################
	
	# Llegim la taula "pedidos"
	elif opcio == 2: 
		
		try:			
				cur.execute("SELECT * FROM pedidos");
				rows = cur.fetchall()
				
				os.system('clear')
				
				print "NUM_PEDIDO FECHA_PEDIDO   CLIE     REP   FAB  PRODUCTO   CANT   IMPORTE "
				print "------------------------------------------------------------------------"
				
				for row in rows:
				   #print row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]
				   print(" {:^10} {} {:^10} {:^5} {:^5} {:^10} {:^5} {:^10} ".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
			
				tecla = raw_input('Prem una tecla per continuar')
		
		except psycopg2.Error as er :
			print "-------- ERROR:", er.pgcode, " -------- \n"
			conn.rollback()

	elif opcio == 3: 
		
		try:	
						
				cur.execute("SELECT * FROM clientes");
				rows = cur.fetchall()
				
				os.system('clear')
				
				print "  num_clie        empresa        rep_clie   limite_credito  "
				print "------------------------------------------------------------"
				
				for row in rows:
				   #print row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]
				   print(" {:^10} {:^20} {:^10} {:^5} ".format(row[0], row[1], row[2], row[3]))
			
				tecla = raw_input('Prem una tecla per continuar')
		
		except psycopg2.Error as er :
			print "-------- ERROR:", er.pgcode, " -------- \n"
			conn.rollback()

############## Productos			
	elif opcio == 4: 
		
		try:	
						
				cur.execute("SELECT * FROM productos");
				rows = cur.fetchall()
				
				os.system('clear')
				
				print " id_fab | id_producto |    descripcion    | precio  | existencias" 
				print " -------+-------------+-------------------+---------+-------------"

				
				for row in rows:
				   #print row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]
				   print(" {:^6} {:^13} {:^20} {:^10} {:^13} ".format(row[0], row[1], row[2], row[3], row[4]))
			
				tecla = raw_input('Prem una tecla per continuar')
		
		except psycopg2.Error as er :
			print "-------- ERROR:", er.pgcode, " -------- \n"
			conn.rollback()
			
############### Oficinas
	elif opcio == 5: 
		
		try:	
						
				cur.execute("SELECT * FROM oficinas");
				rows = cur.fetchall()
				
				os.system('clear')
				
				print "  oficina |   ciudad    | region | dir | objetivo  |  ventas   "
				print " ---------+-------------+--------+-----+-----------+-----------"

				
				for row in rows:
				   #print row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]
				   print(" {:^8} {:^14} {:^8} {:^5} {:^11} {:^10} ".format(row[0], row[1], row[2], row[3], row[4], row[5]))
			
				tecla = raw_input('Prem una tecla per continuar')
		
		except psycopg2.Error as er :
			print "-------- ERROR:", er.pgcode, " -------- \n"
			conn.rollback()			
			
################ Repventas
	elif opcio == 6: 
			
			try:	
							
					cur.execute("SELECT * FROM repventas");
					rows = cur.fetchall()
					
					os.system('clear')
					
					print " num_empl |    nombre     | edad | oficina_rep |   titulo   |  contrato  | director |   cuota   |  ventas   "
					print "----------+---------------+------+-------------+------------+------------+----------+-----------+-----------"

					
					for row in rows:
					   #print row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]
					   print(" {:^8} {:^17} {:^5} {:^14} {:^10}   {}   {:^8} {:^12} {:^12} ".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
				
					tecla = raw_input('Prem una tecla per continuar')
			
			except psycopg2.Error as er :
				print "-------- ERROR:", er.pgcode, " -------- \n"
				conn.rollback()						

##############################################
#        Ens desconnectem de la BBDD         #
##############################################
conn.close()
