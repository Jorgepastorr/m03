salir=False

# Leemos fuera del bucle la primera vez
print "Introduzca -1 para acabar"
num=input("Introduzca un numero: ")

# Condicion de salida
if ( num==-1 ):
	salir=True



while (salir==False):
	# Hacer cosas
	print num
	

	# Leemos dentro del bucle el resto de veces
	print "Introduzca -1 para acabar"
	num=input("Introduzca un numero: ")

	# Condicion de salida
	if ( num==-1 ):
		salir=True


#######################################################3
#		ejemplo
################################################
def leer_apuesta(saldo,salir,apuesta):
	
	if (saldo<10):
		salir_apuesta=True
		salir=True
	else:	
		salir_apuesta=False
		print "Saldo actual:" , saldo
		print "Apuesta mínima 10€"
		print "Salir: -1"
		apuesta=input("Introduca su apuesta: ")
			
	while (salir_apuesta==False):
		if (apuesta==-1):
			salir_apuesta=True
			salir=True
		else:
			if (apuesta>=10 and apuesta<=saldo):
				saldo=saldo-apuesta
				salir_apuesta=True
			else:
				print "Apuesta incorrecta"
				if (apuesta<10):
					print "La apuesta mínima es de 10€"
				if (apuesta>saldo):
					print "No puede apostar más de su saldo"
				print "Salir: -1"
				apuesta=input("Introduca su apuesta: ")
	
	return saldo,salir,apuesta
	
