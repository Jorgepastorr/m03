# coding:utf-8
# ---------------------------------------------------------------
# a               : entrada
# resultado       : salida 

# una vez dentro del def puedes cambiarle el nombre a la variable
# al salir del def seguiran teniendo el nombre anterior  
# ---------------------------------------------------------------
def es_par(a):
	resultado=False
	
	if (a%2==0):
		resultado=True
	
	return resultado
	
	
#############################################################################	

num=0

num=input("Introduce un número:")
# ---------------------------------------------------------------
# num               : entrada
# ---------------------------------------------------------------
if es_par(num):
	print "Es par"
else:
	print "Es impar"




