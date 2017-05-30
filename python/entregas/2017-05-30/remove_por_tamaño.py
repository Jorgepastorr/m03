#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


carpeta="./carpeta-script"

for root, dirs, archivos in os.walk(carpeta):
	
	for name in archivos:
		ruta=os.path.join(root,name)
		peso=os.path.getsize(ruta)
		
		if peso > ((2**10)*150):
				
			print ruta
			print peso
			os.remove(ruta)
			
					
	for name in dirs:
		ruta=os.path.join(root,name)
		peso=os.path.getsize(ruta)
		
		if peso > ((2**10)*150):
				
			print ruta
			print peso
			os.rmdir(ruta)
		
