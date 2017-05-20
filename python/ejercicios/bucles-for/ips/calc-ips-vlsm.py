#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################33
#       calculadora de ip vlsm solo clase c y da 1 red
###################################################33
################
import os
os.system("clear")

###################################################33
#             niveles
###################################################33

#############  define un range 
def mi_rango(inicio,fin,incremento):
	while inicio <= fin :
		yield inicio
		
		inicio=inicio+incremento

############### asigna bits de mac saliente
def control_de_host(host,bits,vuelta):

	if ( host >= 0 and host <= 2 ):
		host_utiles=2
		bits_masc=32-2
	elif ( host >= 3 and host <= 6 ):
		host_utiles=6
		bits_masc=32-3
	elif ( host >= 7 and host <= 14 ):
		host_utiles=14
		bits_masc=32-4
	elif ( host >= 15 and host <= 30 ):
		host_utiles=30
		bits_masc=32-5
	elif ( host >= 31 and host <= 62 ):
		host_utiles=62
		bits_masc=32-6
	elif ( host >= 63 and host <= 126 ):
		host_utiles=126
		bits_masc=32-7
	elif ( host >= 127 and host <= 254 ):
		host_utiles=254
		bits_masc=32-8
	
	else:
		print "no acepto tantos host"
	if bits_masc < bits :
		print "No caben tantos host con esa mac inicial "
		print "deberia se como máximo de",bits_masc,"bits."
	
	if vuelta == 1:
		print "bits mascara nueva",bits_masc
	
	return bits_masc,host_utiles

#####################3

################### comvierte en vinaria la mascara inicial
def macara_ini_a_masc_binaria(mascara_inicial,mi_rango):
	var = 0
	mascara_binaria=[]
	bits=0

	for vueltas in mi_rango(1,4,1) :
		numero = mascara_inicial[var]
		for vueltas in mi_rango(1,8,1) :

			if vueltas == 1:
				if numero%2==1:
					a="1"
					bits=bits+1
				elif numero%2==0:
					a="0"

			else: 
				if numero/2%2==1 :
					a="1"+a
					bits=bits+1
				elif numero/2%2==0 :
					a="0"+a
				
				numero= numero/2
		var=var+1

		int(float(a))
		mascara_binaria.append(int(a))


	print mascara_binaria
	print "bits masara inicial",bits
	
	return mascara_binaria,bits

###########################
#################### nueva mascara en bonario y decimal

def nueva_mascara(bits_masc,mi_rango,vuelta):
	unos=1
	a= ""
	nueva_masc_bin=[]

	# da 32 vueltas número de bits totales de una mac
	for fila in mi_rango(1,4,1) :
		for col in mi_rango(1,8,1) :
			# inserta 1 asta el número de bits elejidos
			if unos <= bits_masc :
				a=a+"1"
			# cuando pasa de bits elegidos inserta 0
			else:
				a=a+"0"
			
			unos=unos+1
		
		# convierte números alfabeticos en numericos y lo inserta en lista (li)
		int(float(a))
		nueva_masc_bin.append(int(a))
		a=""

	
	######################## binario a decimal

	resultado= 0
	final= 0
	masc_final=[]
	var = 0
	# da 4 vueltas 1 por octeto y 8 una por cada bit
	for lista in mi_rango(1,4,1):
		for vuelta in mi_rango(0,7,1):
			if vuelta == 0:
				# diviode el num binario entre 10 si el resto da 1
				# suma 2^vuelta a final si no dfa 1 no tiene que suma nada
				if nueva_masc_bin[var]%10==1 :
					final = 2**vuelta
				resultado = nueva_masc_bin[var] // 10 
			
			else:
				if resultado%10==1 :
					final= final+2**vuelta
				resultado = resultado // 10 
		
		# añade el resultado de cada octeto en la lista mac
		masc_final.append(final)
		# suma 1 a var para cambiar de octeto
		var=var+1
		# resetea contadores para volver a sumar
		resultado= 0
		final= 0
	
	if vuelta == 1:
		# mascara final binaria
		print nueva_masc_bin
		# mascara final decimal
		print masc_final
	
	return nueva_masc_bin,masc_final		
	
##################### datos de entrada y pequeño control
def	control_de_entrada(ip,mascara_inicial,host,posibles_mascaras):	
	

	salir=False
	while salir == False:
		### control de ip
		try:
			print "Separa los octetos por comas."
			ip=input("ip: ")
			salir=True
		except:
			os.system("clear")
			print "lo siento introduces algun dato mal"	
		
	##### contrl de macaras incorrectas
	salir_mascara=False
	while salir_mascara == False:
		try:
			mascara_inicial=input("mascara: ")
			if ((mascara_inicial[3] not in posibles_mascaras) or
				(mascara_inicial[2] not in posibles_mascaras) or
				(mascara_inicial[1] not in posibles_mascaras) or
				(mascara_inicial[0] not in posibles_mascaras) or
				(mascara_inicial[0] < mascara_inicial[1]) or
				(mascara_inicial[1] < mascara_inicial[2]) or
				(mascara_inicial[2] < mascara_inicial[3])):
				os.system("clear")
				print "Esa mascara no es correcta"
			else:
				salir_mascara= True
		except:
			os.system("clear")
			print "Parametros incorrectos"
	#####
	#### control host
	salir_host=False
	while salir_host == False:
		try:
			if mascara_inicial[0] < 255  :
				num_host_posibles= ((254 - mascara_inicial[0])*(255*3)) 
			elif mascara_inicial[1] < 255 :
				num_host_posibles= ((254 - mascara_inicial[1])*(255*2))
			elif mascara_inicial[2] < 255 :
				num_host_posibles= ((254 - mascara_inicial[2])*255)
			elif mascara_inicial[3] < 255 :
				num_host_posibles= (254 - mascara_inicial[3])
				
			print "Número máximo de host: ",num_host_posibles
			host=input("Cuantos host quieres : ")
			if host < 2:
				os.system("clear")
				print "como mínimo necesitas 2 host"
		
			elif num_host_posibles < host:
				os.system("clear")
				print "Demasiados host"
			
			else:
				salir_host =True
		except:
			os.system("clear")
			print "Parametros incorrectos"
	#########33


	return ip,mascara_inicial,host
###################################################33
#      codigo
###################################################33
###################################################33

ip=[]
mascara_inicial=[]
host=[]
posibles_mascaras=[0,128,192,224,240,248,252,254,255]

	# datos de entrada con control de errores
ip,mascara_inicial,host = control_de_entrada(ip,mascara_inicial,host,posibles_mascaras)

# pasa la mascara inicial a binaria
mascara_binaria,bits = macara_ini_a_masc_binaria(mascara_inicial,mi_rango)

#bucle de subrede por hacer
########

rondas =0
octeto3=0

for vuelta in mi_rango(1,3,1):

# calcula si caben los host
	bits_masc,host_utiles = control_de_host(host,bits,vuelta)

# hace mascara nueva tanto binario como decimal
	nueva_masc_bin,masc_final = nueva_mascara(bits_masc,mi_rango,vuelta)

#####################














###################################################33
###################################################33
###################################################33
#  construcción falta clase solo esta la clase C
###################################################33
	if mascara_inicial[0] < 255  :
		var = 0
	elif mascara_inicial[1] < 255 :
		var = 1
	elif mascara_inicial[2] < 255 :
		var = 2
	elif mascara_inicial[3] < 255 :
		var = 3
############### calcula ip
	
	
	for fila in mi_rango(0,0,1):

		print rondas," ",
		for col in mi_rango(1,5,1):
			if vuelta==1 and fila == 0:
				if col == 1:
					print "       red        ",
				elif col ==2:
					print "    Primer host   ",
				elif col ==3:
					print "    Ultimo host    ",
				elif col ==4:
					print "       Brodcast      ",
				elif col ==5:
					print "       Mascara      ",
					
			else:
				if var == 3:
							
					if col == 1:
						print ip[:var],octeto3," ",
					elif col ==2:
						print ip[:var],octeto3+1," ",
					elif col ==3:
						print ip[:var],octeto3+host_utiles," ",					
					elif col ==4:
						print ip[:var],octeto3+host_utiles+1," ",	
						octeto3 = octeto3+host_utiles+2
					elif col ==5:
						print masc_final,
			
		rondas=rondas+1
			
		print ""
