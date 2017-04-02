#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system('clear')

print "SWAP. Intercambio de variables"
print "mano_der=movil"
print "mano_izq=bocadillo"
print "Pista: Usar una variable temporal mano_extra"
print
########### modo 1 de hacerlo BUENO BUENo ##############
der="movil"
izq="bocadillo"
der ,izq = izq, der  ## intercabia variables a la vez ##
print "modo 1 "
print "mano der "+der
print "mano izq "+izq
##################################

############### modo joni  ####################
print
print "modo 2"
print "derecha  mobil"
print "izquierda bocata"
print
######
de = "mobil"
iz = "bocata"

extra = de
de = iz
iz = extra 
######
print "mano der "+de
print "mano izq "+iz
########################################
