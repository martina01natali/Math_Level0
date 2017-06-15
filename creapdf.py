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

# trasforma in pdf tutti i file .tex presenti nella directory:
$ creapdf.py

# trasforma in pdf il o i file .tex passato come argomento:
$ creapdf.py pippo.tex pluto.tex

# opzione -t fa una sola compilazione e non cancella i file ausiliari:
$ creapdf.py -t

"""
from __future__ import division, print_function

import sys, getopt
import os

def topdf(filename, test):
    """Compile with: pdflatex <filename>."""
    os.system('pdflatex --shell-escape ' + filename)
    if not test:
        os.system('pdflatex --shell-escape ' + filename)
        os.system('make clean')

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, nfiles = getopt.getopt(argv,"hti:o:",["ifile=","ofile="])
##        print(opts, args)
    except(getopt.GetoptError):
        print(__doc__)
        sys.exit(2)
    ptest = False
    for opt, arg in opts:
        if opt == '-h':
             print(__doc__)
             sys.exit()
        if opt == '-t':
             ptest = True
##      elif opt in ("-i", "--ifile"):
##         inputfile = arg
##      elif opt in ("-o", "--ofile"):
##         outputfile = arg
##   print('Input file is "', inputfile)
##   print('Output file is "', outputfile)
    if nfiles == []:
        nfiles = [n_f for n_f in os.listdir('.') if n_f.endswith('.tex')]
    for filename in nfiles:
        topdf(filename, ptest)

if __name__ == "__main__":
    main(sys.argv[1:])

