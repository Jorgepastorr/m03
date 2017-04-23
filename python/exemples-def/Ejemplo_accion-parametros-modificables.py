# coding:utf-8

# PARAMETROS
# ---------------------------------------------------------------
# nombre          : entrada          valor       no modificable
# apellido1       : entrada/salida   referencia  modificable
# apellido2       : entrada/salida   referencia  modificable
# nombre_completo : salida           referencia  modificable
# ---------------------------------------------------------------
def mensaje_bienvenida(nombre, apellido1, apellido2):
	print "*****************************"
	print "          BIENVENIDO         "
	print " ", nombre , "," , apellido1, "," , apellido2
	print "*****************************"
	
	nombre_completo=nombre+","+apellido1+" "+apellido2
	
	apellido1="CAMBIAZO"
	apellido2="CAMBIAZON"
	
	
	
	return apellido1,apellido2,nombre_completo
	
#############################################################################	

nombre_invitado="PEPE"
apellido1_invitado="SANCHEZ"
apellido2_invitado="LOPEZ"
nombre_completo_invitado=""

print nombre_invitado , apellido1_invitado, apellido2_invitado,nombre_completo_invitado


# ----------------------------------------------------------------------
# nombre_invitado          : entrada          valor       no modificable
# apellido1_invitado       : entrada/salida   referencia  modificable
# apellido2_invitado       : entrada/salida   referencia  modificable
# nombre_completo_invitado : salida           referencia  modificable
# ----------------------------------------------------------------------
apellido1_invitado,apellido2_invitado,nombre_completo_invitado=mensaje_bienvenida(nombre_invitado,apellido1_invitado,apellido2_invitado)


# Sólo cambia el valor de los parámetro modificables
print  apellido1_invitado, apellido2_invitado,nombre_completo_invitado
