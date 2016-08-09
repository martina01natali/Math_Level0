#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------python----------------------creapdf.py--#
#                                                                       #
#                           da LaTeX a pdf                              #
#                                                                       #
#--Daniele Zambelli--------------GPL------------------------------2016--#

"""
Manda in compilazione latex il file o i files .tex
passati come argomento.

Uso:

$ creapdf.py pippo.tex

$ creapdf.py pippo.tex pluto.tex

"""
from __future__ import division, print_function

import sys, getopt
import os

def topdf(filename):
    """Compile with: pdflatex <filename>."""
    os.system('pdflatex --shell-escape ' + filename)

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
##        print(opts, args)
    except(getopt.GetoptError):
        print(__doc__)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
             print(__doc__)
             sys.exit()
##      elif opt in ("-i", "--ifile"):
##         inputfile = arg
##      elif opt in ("-o", "--ofile"):
##         outputfile = arg
##   print('Input file is "', inputfile)
##   print('Output file is "', outputfile)
    if args == []:
        print(__doc__)
        sys.exit()
    for filename in args:
        topdf(filename)

if __name__ == "__main__":
    main(sys.argv[1:])

