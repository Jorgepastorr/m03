#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,stat

carpeta="./carpeta-script"

lista_ruta=[]
lista=[]
# mira permisos que tienen las carpetas
for root, dirs, archivos in os.walk(carpeta):	
	total_archivos=dirs+archivos
	for name in total_archivos:
		ruta=os.path.join(root,name)
		permisos=stat.S_IMODE(os.stat(ruta).st_mode)
		permisos=oct(permisos)

		if permisos[3] == "7":
			lista_ruta.append(ruta)
			lista.append(ruta+"  "+permisos)

print "Tiene un fallo de seguridad en estos archivos: "
for i in lista:
	print i
			
var=input("\n1-si \n2-no \nQuiere cambiar los permisos de otros? ")
	
if var == 1:
	 cambio=input("inserta los nuevos permisos deseados: \nrecomiendo 0755: ")	
	 for i in lista_ruta :
		 os.chmod(i,cambio)
		 permisos=stat.S_IMODE(os.stat(i).st_mode)
		 permisos=oct(permisos)
		 #print i,permisos
		 print '{0:50} {1:5}  '.format(i,permisos)
else:
	print "\nAdios"
