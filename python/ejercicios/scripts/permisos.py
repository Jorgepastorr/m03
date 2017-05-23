#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

carpeta="./carpeta-script"


#cambia permisos de carpeta a 700 y ficheros 777
for root, dirs, archivos in os.walk(carpeta):	
	for name in archivos:
		ruta=os.path.join(root,name)
		os.chmod(ruta,0700)
		
		
	for name in dirs:
		ruta=os.path.join(root,name)
		os.chmod(ruta,0777)
		
