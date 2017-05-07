#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
a1=1
a2=2

numero= input("numero: ")
fila= raw_input("fila: ")
columna=raw_input("columna: ")

casilla=(fila+columna)
asignacion={"A1":a1,"A2":a2}

asignacion[casilla]=numero

print a1
print a2
print asignacion[casilla]
