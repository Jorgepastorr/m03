#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################
def control_casillas_originales(casilla):

	#### variables salia sudoku 1
	a1,a2,a3,a4,a5,a6,a7,a8,a9=0,8,0,0,0,0,0,0,0
	b1,b2,b3,b4,b5,b6,b7,b8,b9=9,5,0,0,6,0,7,0,4
	c1,c2,c3,c4,c5,c6,c7,c8,c9=3,0,0,0,0,0,0,0,9
	d1,d2,d3,d4,d5,d6,d7,d8,d9=0,2,0,0,0,0,0,0,0
	e1,e2,e3,e4,e5,e6,e7,e8,e9=0,0,4,0,0,5,0,0,0
	f1,f2,f3,f4,f5,f6,f7,f8,f9=7,1,0,0,0,2,9,4,0
	g1,g2,g3,g4,g5,g6,g7,g8,g9=0,6,8,0,2,0,0,7,3
	h1,h2,h3,h4,h5,h6,h7,h8,h9=0,0,0,4,5,0,6,0,8
	i1,i2,i3,i4,i5,i6,i7,i8,i9=4,0,2,6,3,0,0,9,5

	if casilla =! 0 :
		print "No puedes cambiar ese número. \nEs del sudoku original."
	else:	
		salir_raw=True

	return salir_raw
	
################################33

salir_raw = control_casillas_originales(casilla)
