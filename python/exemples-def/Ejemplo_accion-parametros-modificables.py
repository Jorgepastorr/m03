# coding:utf-8

# PARAMETROS
# ---------------------------------------------------------------
# nombre          : entrada          valor       no modificable
# apellido1       : entrada/salida   referencia  modificable
# apellido2       : entrada/salida   referencia  modificable
# nombre_completo : salida           referencia  modificable
# ---------------------------------------------------------------
def mensaje_bienvenida(nombre, ape_1, ape_2):
	print "*****************************"
	print "          BIENVENIDO         "
	print " ", nombre , "," , ape_1, "," , ape_2
	print "*****************************"
	
	nombre_completo = nombre+","+ape_1+" "+ape_2
	
	ape_1="CAMBIAZO"
	ape_2="CAMBIAZON"
	
	
	
	return ape_1,ape_2,nombre_completo
	
#############################################################################	

nombre="PEPE"
apellido1="SANCHEZ"
apellido2="LOPEZ"
nombre_completo=""

print nombre , apellido1, apellido2,nombre_completo


# ----------------------------------------------------------------------
# nombre                   : entrada          valor       no modificable
# apellido1                : entrada/salida   referencia  modificable
# apellido2                : entrada/salida   referencia  modificable
# nombre_completo          : salida           referencia  modificable
# ----------------------------------------------------------------------
apellido1,apellido2,nombre_completo=mensaje_bienvenida(nombre,apellido1,apellido2)


# Sólo cambia el valor de los parámetro modificables
print  apellido1, apellido2,nombre_completo
