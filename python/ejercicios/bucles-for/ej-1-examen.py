# coding: utf-8


def mi_rango(inicio,final,incremento):
	
	if inicio <= final :
		while inicio <= final :
			yield inicio
			inicio = inicio + incremento
	else:
		while inicio >= final :
			yield inicio
			inicio = inicio - incremento
		
#############3
		
for fila in mi_rango(1,4,1):
	for columna in mi_rango(1,6,1):
		if (fila == 1) or (fila == 4 ):
			print "*",
		
		elif ( columna == 1 ) or ( columna == 6 ):
			print "*",
		else:
			if (fila == 2) and (columna == 3 or columna == 4 ):
				print "·",
			
			elif ( fila == 3 and columna == 3 ):
				print "\\",
			
			elif ( fila == 3 and columna == 4 ):
				print "/",
			
			else:
				print " ",
	print " "
