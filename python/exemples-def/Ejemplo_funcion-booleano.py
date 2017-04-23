# coding:utf-8
def es_par(a):
	resultado=False
	
	if (a%2==0):
		resultado=True
	
	return resultado
	
	
#############################################################################	

num=0

num=input("Introduce un número:")

if es_par(num):
	print "Es par"
else:
	print "Es impar"




