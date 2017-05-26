#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,stat

carpeta="./carpeta-script"

lista=[]
# mira permisos que tienen las carpetas
for root, dirs, archivos in os.walk(carpeta):	
	total_archivos=dirs+archivos
	for name in total_archivos:
		ruta=os.path.join(root,name)
		permisos=stat.S_IMODE(os.stat(ruta).st_mode)
		permisos=oct(permisos)

		if permisos[3] == "7":
			lista.append(ruta+"  "+permisos)

print "Tiene un fallo de seguridad en estos archivos: "
for i in lista:
	print i
			
			
