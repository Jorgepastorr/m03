#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


carpeta="./carpeta-script"


# muestra ruta de archivos
for root, dirs, archivos in os.walk(carpeta):
	for name in archivos:
		ruta=os.path.join(root,name)
		print ruta
		
print "--------------------------------"
	
# ruta y peso de archivos
for root, dirs, archivos in os.walk(carpeta):
	for name in archivos:
		ruta=os.path.join(root,name)
		peso=os.path.getsize(ruta)
		print ruta
		print peso

print "--------------------------------"

# muestra ruta de todos los archivos y carpetas y su peso
for root, dirs, archivos in os.walk(carpeta):
	total_archivos=dirs+archivos
	for name in total_archivos:
		ruta=os.path.join(root,name)
		peso=os.path.getsize(ruta)
		print ruta
		print peso

print "--------------------------------"

peso_total=0
# muestra peso completo de la carpeta y sus archvos
for root, dirs, archivos in os.walk(carpeta):
	total_archivos=dirs+archivos
	
	for name in total_archivos:
		ruta=os.path.join(root,name)
		peso=os.path.getsize(ruta)
		
		peso_total=peso_total+peso

print "Peso total, carpetas mas archivos."
print peso_total,"KB"
print peso_total/1024,"MB"

print "--------------------------------"

peso_total_archivos=0
peso_total_dirs=0
# muestra peso completo de la carpeta y sus archvos por separado
for root, dirs, archivos in os.walk(carpeta):	
	for name in archivos:
		ruta=os.path.join(root,name)
		peso=os.path.getsize(ruta)
		
		peso_total_archivos=peso_total_archivos+peso

	for name in dirs:
		ruta=os.path.join(root,name)
		peso=os.path.getsize(ruta)
		
		peso_total_dirs=peso_total_dirs+peso

print "Peso total archivos."
print peso_total_archivos,"KB"
print peso_total_archivos/1024,"MB"

print "Peso total carpetas."
print peso_total_dirs,"KB"
print peso_total_dirs/1024,"MB"

print "--------------------------------"

























