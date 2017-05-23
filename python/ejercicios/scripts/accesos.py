#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from datetime import datetime,date

carpeta="./carpeta-script"


formato = '%d-%m-%y %H:%M:%S' 
# muestra ultimo acceso
for root, dirs, archivos in os.walk(carpeta):
	# juunta carpetas y ficheros en 1 lista
	total_archivos=dirs+archivos
	for name in total_archivos:
		# busca la ruta de cada archivo
		ruta=os.path.join(root,name)
		# ni p... idea 
		estado=os.stat(root+os.sep+name)
		
		# define el ultimo acceso y modificación
		ult_acceso = datetime.fromtimestamp(estado.st_atime)
		modificado = datetime.fromtimestamp(estado.st_mtime)
		# lo añade en formato bonito
		ult_acceso = ult_acceso.strftime(formato)
		modificado = modificado.strftime(formato)		
		##

		print ""
		print ruta
		print "Ultima modificación: ",modificado
		print "Ultimo acceso:       ",ult_acceso
print "--------------------------------"
