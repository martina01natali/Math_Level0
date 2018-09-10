#!/usr/bin/python3
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

# trasforma in pdf tutti i file .tex presenti nella directory e
  produce pdf monocromatici:
$ ./creapdf.py

# trasforma in pdf i file .tex passati come argomento e
  produce un pdf monocromatico:
$ ./creapdf.py pippo.tex pluto.tex

# opzione -t (test) fa una sola compilazione,
  non cancella i file ausiliari e non produce il pdf monocromatico:
$ ./creapdf.py -t

"""
##from __future__ import division, print_function

import sys, getopt
import os

def topdf(filename, test):
    """Compile with: pdflatex <filename>."""
    nfile = filename[:-4]
    print(nfile)
    os.system('pdflatex --shell-escape ' + filename)
    if not test:
        os.system('pdflatex --shell-escape ' + filename)
        os.system('make clean')
        GSLINE = rf"gs -sDEVICE=pdfwrite \
-dProcessColorModel=/DeviceGray \
-dColorConversionStrategy=/Gray \
-dPDFUseOldCMS=false \
-o {nfile}_mono.pdf -f {nfile}.pdf"
        os.system(GSLINE)

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

