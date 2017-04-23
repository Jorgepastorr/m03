# coding:utf-8

# PARAMETROS
# ---------------------------------------------------------------
# a               : entrada
# b               : entrada
# resultado       : salida   
# ---------------------------------------------------------------
def sumar(a,b):
	resultado=0
	
	resultado=a+b
	
	return resultado
	
	
#############################################################################	
num1=0
num2=0


num1=input("Introduce número1: ")
num2=input("Introduce número2: ")

# PARAMETROS
# ---------------------------------------------------------------
# num2          : entrada  
# num1          : entrada  
# ---------------------------------------------------------------
total=sumar(num1,num2)

print "La suma de " , num1, " y " , num2, "es igual a ", total

