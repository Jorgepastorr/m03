# coding:utf-8
def mensaje_bienvenida(nombre, apellido):
	print "*****************************"
	print "          BIENVENIDO         "
	print "       	", nombre , "," , apellido
	print "*****************************"
	
	nombre="CAMBIO"
	apellido="CAMBIAZO"
	
#############################################################################	

nombre_invitado="PEPE"
apellido_invitado="SANCHEZ"

print nombre_invitado , apellido_invitado

mensaje_bienvenida(nombre_invitado,apellido_invitado)


# Los parámetros no son modificables
# Aunque se cambie su valor dentro de la acción
print nombre_invitado , apellido_invitado
