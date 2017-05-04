#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
cont=1
for fila in xrange(1,10):
	print ""
	for columna in xrange(1,4):
		if columna == 1:
			print fila,
		elif columna == 2:
			print "A",
		elif columna == 3:
			print cont,
			if fila%3==0:
				cont=cont+1
