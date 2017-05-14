#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################33
#       calculadora de ip vlsm solo clase c y da 1 red
###################################################33
################
import os

###################################################33
#             niveles
###################################################33

#############  define un range 
def mi_rango(inicio,fin,incremento):
	while inicio <= fin :
		yield inicio
		
		inicio=inicio+incremento

############### asigna bits de mac saliente
def control_de_host(host,bits):

	if ( host >= 0 and host <= 4 ):
		host_utiles=2
		bits_masc=32-2
	elif ( host >= 5 and host <= 8 ):
		host_utiles=6
		bits_masc=32-3
	elif ( host >= 9 and host <= 16 ):
		host_utiles=14
		bits_masc=32-4
	elif ( host >= 17 and host <= 32 ):
		host_utiles=30
		bits_masc=32-5
	elif ( host >= 33 and host <= 64 ):
		host_utiles=62
		bits_masc=32-6
	elif ( host >= 65 and host <= 128 ):
		host_utiles=126
		bits_masc=32-7
	elif ( host >= 129 and host <= 256 ):
		host_utiles=254
		bits_masc=32-8
	
	else:
		print "no acepto tantos host"
	if bits_masc < bits :
		print "No caben tantos host con esa mac inicial "
		print "deberia se como máximo de",bits_masc,"bits."
	
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

def nueva_mascara(bits_masc,mi_rango):
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

	# mascara final binaria
	print nueva_masc_bin
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
	
	# mascara final decimal
	print masc_final
	
	return nueva_masc_bin,masc_final		
	
##################### datos de entrada y pequeño control
def	control_de_entrada(salir,ip,mascara_inicial,host):	
	
	try:
		print "Separa los octetos por comas."
		ip=input("ip: ")
	
		mascara_inicial=input("mascara: ")
		
		print "Número máximo de host: ",255-mascara_inicial[3]
		host=input("Cuantos host quieres : ")
		if host < 2:
			os.system("clear")
			print "como mínimo necesitas 2 host"
	
		elif 255-mascara_inicial[3] >= host:
			salir=True
	
		else:
			os.system("clear")
			print "Demasiados host"
	except:
		os.system("clear")
		print "lo siento introduces algun dato mal"
		
	return ip,mascara_inicial,host,salir
###################################################33
#      codigo
###################################################33
###################################################33

ip=[]
mascara_inicial=[]
host=[]

salir = False
while salir == False:
	# datos de entrada con control de errores
	ip,mascara_inicial,host,salir = control_de_entrada(salir,ip,mascara_inicial,host)

# pasa la mascara inicial a binaria
mascara_binaria,bits = macara_ini_a_masc_binaria(mascara_inicial,mi_rango)

# calcula si caben los host
bits_masc,host_utiles = control_de_host(host,bits)

# hace mascara nueva tanto binario como decimal
nueva_masc_bin,masc_final = nueva_mascara(bits_masc,mi_rango)

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
fila =0
octeto3=0

#for fila in mi_rango(1,2,1):
while octeto3 < 255:
	print fila," ",
	for col in mi_rango(1,5,1):
		if fila == 0:
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
				if fila == 1:
					if col == 1:
						print ip[:var],mascara_inicial[3]," ",
					elif col ==2:
						print ip[:var],mascara_inicial[3]+1," ",
					elif col ==3:
						print ip[:var],mascara_inicial[3]+host_utiles," ",					
					elif col ==4:
						print ip[:var],mascara_inicial[3]+host_utiles+1," ",	
						octeto3 = mascara_inicial[3]+host_utiles+2
					elif col ==5:
						print masc_final,
			
				else:
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
			
	fila=fila+1
		
	print ""
