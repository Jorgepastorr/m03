#!/usr/bin/env python
# -*- coding: utf-8 -*-

a1,a2,a3,a4,a5,a6,a7,a8,a9=0,0,0,0,0,0,0,0,0
b1,b2,b3,b4,b5,b6,b7,b8,b9=0,0,0,0,0,0,0,0,0
c1,c2,c3,c4,c5,c6,c7,c8,c9=0,0,0,0,0,0,0,0,0
d1,d2,d3,d4,d5,d6,d7,d8,d9=0,0,0,0,0,0,0,0,0
e1,e2,e3,e4,e5,e6,e7,e8,e9=0,0,0,0,0,0,0,0,0
f1,f2,f3,f4,f5,f6,f7,f8,f9=0,0,0,0,0,0,0,0,0
g1,g2,g3,g4,g5,g6,g7,g8,g9=0,0,0,0,0,0,0,0,0
h1,h2,h3,h4,h5,h6,h7,h8,h9=0,0,0,0,0,0,0,0,0
i1,i2,i3,i4,i5,i6,i7,i8,i9=0,0,0,0,0,0,0,0,0

def sudoku(a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9):

	print ""
	print "    1   2   3   4   5   6   7   8   9"
	print "\033[;31m"+"  ______________________________________"+"\033[0;m"
	print "A||",a1,"|",a2,"|",a3,"\033[;31m"+":"+"\033[0;m",a4,"|",a5,"|",a6,"\033[;31m"+":"+"\033[0;m",a7,"|",a8,"|",a9,"||"
	print "  -------------------------------------"
	print "B||",b1,"|",b2,"|",b3,"\033[;31m"+":"+"\033[0;m",b4,"|",b5,"|",b6,"\033[;31m"+":"+"\033[0;m",b7,"|",b8,"|",b9,"||"
	print "  -------------------------------------"
	print "C||",c1,"|",c2,"|",c3,"\033[;31m"+":"+"\033[0;m",c4,"|",c5,"|",c6,"\033[;31m"+":"+"\033[0;m",c7,"|",c8,"|",c9,"||"
	print "\033[;31m"+"  ======================================"+"\033[0;m"
	print "D||",d1,"|",d2,"|",d3,"\033[;31m"+":"+"\033[0;m",d4,"|",d5,"|",d6,"\033[;31m"+":"+"\033[0;m",d7,"|",d8,"|",d9,"||"
	print "  -------------------------------------"
	print "E||",e1,"|",e2,"|",e3,"\033[;31m"+":"+"\033[0;m",e4,"|",e5,"|",e6,"\033[;31m"+":"+"\033[0;m",e7,"|",e8,"|",e9,"||"
	print "  -------------------------------------"
	print "F||",f1,"|",f2,"|",f3,"\033[;31m"+":"+"\033[0;m",f4,"|",f5,"|",f6,"\033[;31m"+":"+"\033[0;m",f7,"|",f8,"|",f9,"||"
	print "\033[;31m"+"  ======================================"+"\033[0;m"
	print "G||",g1,"|",g2,"|",g3,"\033[;31m"+":"+"\033[0;m",g4,"|",g5,"|",g6,"\033[;31m"+":"+"\033[0;m",g7,"|",g8,"|",g9,"||"
	print "  -------------------------------------"
	print "H||",h1,"|",h2,"|",h3,"\033[;31m"+":"+"\033[0;m",h4,"|",h5,"|",h6,"\033[;31m"+":"+"\033[0;m",h7,"|",h8,"|",h9,"||"
	print "  -------------------------------------"
	print "I||",i1,"|",i2,"|",i3,"\033[;31m"+":"+"\033[0;m",i4,"|",i5,"|",i6,"\033[;31m"+":"+"\033[0;m",i7,"|",i8,"|",i9,"||"
	print "\033[;31m"+"  ______________________________________"+"\033[0;m"
	print ""
	return a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9


a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9=sudoku(a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9,c1,c2,c3,c4,c5,c6,c7,c8,c9,d1,d2,d3,d4,d5,d6,d7,d8,d9,e1,e2,e3,e4,e5,e6,e7,e8,e9,f1,f2,f3,f4,f5,f6,f7,f8,f9,g1,g2,g3,g4,g5,g6,g7,g8,g9,h1,h2,h3,h4,h5,h6,h7,h8,h9,i1,i2,i3,i4,i5,i6,i7,i8,i9)