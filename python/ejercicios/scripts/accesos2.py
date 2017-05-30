#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,time

import calendar

carpeta="./carpeta-script"

for root, dirs, archivos in os.walk(carpeta):
	total_archivos=dirs+archivos
	
	for name in total_archivos:
		ruta=os.path.join(root,name)
		acceso=time.ctime(os.path.getatime(ruta))
		modificacion=time.ctime(os.path.getmtime(ruta))
		
		
		print ruta
		print "ultimo acceso: ",acceso
		print "ultima modificación: ",modificacion
		print ""


