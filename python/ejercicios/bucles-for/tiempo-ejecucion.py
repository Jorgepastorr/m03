#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Demostració de que xrange genera les llistes
# de manera més eficient
# Millor utilitzar xrange
import time

#use time.time() on Linux

start = time.clock()
for x in range(10000000):
    pass
stop = time.clock()

print "Temps range" , stop - start

start = time.clock()
for x in xrange(10000000):
    pass
stop = time.clock()


print "Temps xrange" ,stop - start

print "-------------------------------"
