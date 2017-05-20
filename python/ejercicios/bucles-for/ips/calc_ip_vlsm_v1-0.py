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
def control_de_host(host,bits,vuelta,redes):

	if ( redes[vuelta] >= 0 and redes[vuelta] <= 2 ):
		host_utiles=2
		bits_masc=32-2
	elif ( redes[vuelta] >= 3 and redes[vuelta] <= 6 ):
		host_utiles=6
		bits_masc=32-3
	elif ( redes[vuelta] >= 7 and redes[vuelta] <= 14 ):
		host_utiles=14
		bits_masc=32-4
	elif ( redes[vuelta] >= 15 and redes[vuelta] <= 30 ):
		host_utiles=30
		bits_masc=32-5
	elif ( redes[vuelta] >= 31 and redes[vuelta] <= 62 ):
		host_utiles=62
		bits_masc=32-6
	elif ( redes[vuelta] >= 63 and redes[vuelta] <= 126 ):
		host_utiles=126
		bits_masc=32-7
	elif ( redes[vuelta] >= 127 and redes[vuelta] <= 254 ):
		host_utiles=254
		bits_masc=32-8
	elif ( redes[vuelta] >= 255 and redes[vuelta] <= 510 ):
		host_utiles=510
		bits_masc=32-9
	elif ( redes[vuelta] >= 511 and redes[vuelta] <= 1022 ):
		host_utiles=1022
		bits_masc=32-10
	elif ( redes[vuelta] >= 1023 and redes[vuelta] <= 2046 ):
		host_utiles=2046
		bits_masc=32-11
	elif ( redes[vuelta] >= 2047 and redes[vuelta] <= 4094 ):
		host_utiles=4094
		bits_masc=32-12
	elif ( redes[vuelta] >= 4095 and redes[vuelta] <= 8190 ):
		host_utiles=8190
		bits_masc=32-13
	elif ( redes[vuelta] >= 8191 and redes[vuelta] <= 16382 ):
		host_utiles=16382
		bits_masc=32-14
	elif ( redes[vuelta] >= 16383 and redes[vuelta] <= 32766 ):
		host_utiles=32766
		bits_masc=32-15
	elif ( redes[vuelta] >= 32767 and redes[vuelta] <= 65534 ):
		host_utiles=65534
		bits_masc=32-16
	
	else:
		print "no acepto tantos host"
	if bits_masc < bits :
		print "No caben tantos host con esa mac inicial "
		print "deberia se como máximo de",bits_masc,"bits."
	
	
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
		for vueltas in mi_rango(0,7,1):
			if vueltas == 0:
				# diviode el num binario entre 10 si el resto da 1
				# suma 2^vuelta a final si no dfa 1 no tiene que suma nada
				if nueva_masc_bin[var]%10==1 :
					final = 2**vueltas
				resultado = nueva_masc_bin[var] // 10 
			
			else:
				if resultado%10==1 :
					final= final+2**vueltas
				resultado = resultado // 10 
		
		# añade el resultado de cada octeto en la lista mac
		masc_final.append(final)
		# suma 1 a var para cambiar de octeto
		var=var+1
		# resetea contadores para volver a sumar
		resultado= 0
		final= 0
		
	return nueva_masc_bin,masc_final		
	
##################### datos de entrada y pequeño control
def	control_de_entrada(ip,mascara_inicial,host,posibles_mascaras,redes):	
	

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
	#### control subredes
	salir_subredes=False
	while salir_subredes == False:
		try:
			subredes=input("Cuantas subredes quieres? ")
			salir_subredes =True
		except:
			os.system("clear")
			print "Parametros incorrectos"
				
		
	if mascara_inicial[0] < 255  :
		num_host_posibles= ((255 - mascara_inicial[0])*(255*3)) 
	elif mascara_inicial[1] < 255 :
		num_host_posibles= ((255 - mascara_inicial[1])*(255*2))
	elif mascara_inicial[2] < 255 :
		num_host_posibles= (((255 - mascara_inicial[2])*255)-1)
	elif mascara_inicial[3] < 255 :
		num_host_posibles= (254 - mascara_inicial[3])

	lista_host=[]
	for i in mi_rango(1, subredes,1):
		## contrl de host
####3 mejorar	la resta de hosts a de ser proporcional a 2^tal-2 y ajustar num_posibles de host	
		salir_host=False
		while salir_host == False:
			try:			
				print "Número máximo de host: ",num_host_posibles
				print "Para red",i
				host = input("Cuantos host quieres? ") 
				os.system("clear")
				
				if host < 2:
					os.system("clear")
					print "como mínimo necesitas 2 host"

				elif num_host_posibles < host:
					os.system("clear")
					print "Demasiados host"
				
				else:
					num_host_posibles=num_host_posibles-host
					lista_host.append(host)
					salir_host =True
			except:
				os.system("clear")
				print "Parametros incorrectos"			
	
	# ordenar lista de mayor a menor
	lista_host.sort(reverse=True)
	
	# asigna en orden descendente el número de red con hosts 
	for x in mi_rango(0, subredes-1,1):
		redes[ x+1 ] = lista_host[x] 
########3 
	#########33
	
	return ip,mascara_inicial,host,redes,subredes
###################################################33
#      codigo
###################################################33
###################################################33
redes={}
ip=[]
mascara_inicial=[]
host=[]
posibles_mascaras=[0,128,192,224,240,248,252,254,255]
rondas =0
octeto4=0
octeto3=0
#ultimo_host del octeto 3
octeto31=0


	# datos de entrada con control de errores
ip,mascara_inicial,host,redes,subredes = control_de_entrada(ip,mascara_inicial,host,posibles_mascaras,redes)

# pasa la mascara inicial a binaria
mascara_binaria,bits = macara_ini_a_masc_binaria(mascara_inicial,mi_rango)

#bucle de subrede por hacer
########

for vuelta in mi_rango(1,subredes,1):

	# calcula si caben los host
#falta agrandar
	bits_masc,host_utiles = control_de_host(host,bits,vuelta,redes)
# host utiles que se van a mostrar en pantalla, los renombro antes de cambiarles el resultado
	host_pantalla=host_utiles
# hace mascara nueva tanto binario como decimal
	nueva_masc_bin,masc_final = nueva_mascara(bits_masc,mi_rango,vuelta)


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
	
	##
	titulos=["   ","       red        ","     Primer host   ","    Ultimo host    ","    Brodcast      ","    Mascara      ","host útiles"]
	if vuelta == 1:
		for i in titulos:
			print i, 			
		print""
		
	for fila in mi_rango(0,0,1):
		print '{0:3}  '.format(vuelta),
		for col in mi_rango(1,5,1):
		
			if var == 3:					
				if col == 1:
					print '{0:3}.{1:3}.{2:3}.{3:3}   '.format(ip[0],ip[1],ip[2],octeto4),
				elif col ==2:
					print '{0:3}.{1:3}.{2:3}.{3:3}   '.format(ip[0],ip[1],ip[2],octeto4+1),
				elif col ==3:
					print '{0:3}.{1:3}.{2:3}.{3:3}   '.format(ip[0],ip[1],ip[2],octeto4+host_utiles),
				elif col ==4:
					print '{0:3}.{1:3}.{2:3}.{3:3}   '.format(ip[0],ip[1],ip[2],octeto4+host_utiles+1),
					octeto4 = octeto4+host_utiles+2
				elif col ==5:
					print '{0:3}.{1:3}.{2:3}.{3:3}   {4:6}'.format(masc_final[0],masc_final[1],masc_final[2],masc_final[3],host_utiles),
					
			elif var == 2:
				
				# si los host_utiles son mas de 254 divide y suma en el octeto 3				
				if host_utiles > 254 :
					while host_utiles > 254:
						host_utiles = host_utiles - 255
						octeto31=octeto31+1
				
				if (octeto4+host_utiles) > 254:
					octeto31 = octeto31+1
					host_utiles = host_utiles-254
							
				if col == 1:
					print '{0:3}.{1:3}.{2:3}.{3:3}   '.format(ip[0],ip[1],octeto3,octeto4),
				elif col ==2:
					print '{0:3}.{1:3}.{2:3}.{3:3}   '.format(ip[0],ip[1],octeto3,octeto4+1),
				elif col ==3:
					print '{0:3}.{1:3}.{2:3}.{3:3}   '.format(ip[0],ip[1],octeto31,octeto4+host_utiles),
				elif col ==4:
					print '{0:3}.{1:3}.{2:3}.{3:3}   '.format(ip[0],ip[1],octeto31,octeto4+host_utiles+1),
					# si octeto 4 llega a 255 suma a octeto 3 +1 y reseta octeto4
					if (octeto4+host_utiles+1) >= 255:
						octeto3 =octeto31
						octeto3 =octeto3+1
						octeto4 =0
					# sino solo suma 2 a octeto4 y sigue	
					else:
						octeto4 = octeto4+host_utiles+2
						octeto3=octeto31
				elif col ==5:
					print '{0:3}.{1:3}.{2:3}.{3:3}   {4:6}'.format(masc_final[0],masc_final[1],masc_final[2],masc_final[3],host_pantalla),
	
				
		rondas=rondas+1
			
		print ""
