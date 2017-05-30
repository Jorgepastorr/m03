#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from datetime import datetime,date,timedelta

carpeta="./carpeta-script"


formato = '%Y-%m-%d'

# muestra ultimo acceso
for root, dirs, archivos in os.walk(carpeta):
	
	for name in archivos:
		# busca la ruta de cada archivo
		ruta=os.path.join(root,name)
		# asigna a peso lo que pesa cada archivo
		peso=os.path.getsize(ruta)
		
		# monta unos modulos para fromtimestamp
		estado=os.stat(root+os.sep+name)
		# define el ultimo acceso y modificación
		ult_acceso = datetime.fromtimestamp(estado.st_atime)
		# lo añade a formate que se pueda comparar
		fecha_final = ult_acceso.strftime(formato)
		##
		# fecha actual - los días indicados
		fecha = datetime.now().date()  -  timedelta(days=365)
		
		# si la ultima modificación es inferior a la indicada 
		# O pesa más de 1G "a la basura"
		if (str(fecha_final) < str(fecha)) or (peso > 2**30):
			# si cumple las condiciones se borra el archivo
			os.remove(ruta)
		


