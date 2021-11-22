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
$ ./creapdf.py -t [<elencofile>]

# opzione -x (xhtml) produce un file xhtml con mathml:
$ ./creapdf.py -x [<elencofile>]

# opzione -j (xhtml) produce un file xhtml con matjax:
$ ./creapdf.py -x [<elencofile>]

# opzione -m (mono) esegue la compilazione e produce il pdf monocromatico:
$ ./creapdf.py -m

# opzione -c (clean) pulisce le directory dai file di supporto:
$ ./creapdf.py -c

"""
##from __future__ import division, print_function

import sys, getopt
import os

DDIR = 'dist'
SAFEDIR = [DDIR, 'copertine', '_ignore', 'html']
EXTCLEAR = ('.4ct', '.4tc', '.aux', '.css', '.dvi', '.gnuplot',
            '.html', '.idv', '.lg', '.log', '.svg', '.ps', '.listing',
            '.nav', '.out', '.snm', '.table', '.tmp', '.toc', '.xref')

def topdf(filename, test, mono):
    """Compile with: pdflatex <filename>."""
    nfile, ext = os.path.splitext(filename)
##    print(filename, '-->', nfile, ext)
    os.system('pdflatex --shell-escape ' + filename)
    if not test:
        os.system('pdflatex --shell-escape ' + filename)
##        os.system('make clean')
    if mono:
        GSLINE = rf"gs -sDEVICE=pdfwrite \
-dProcessColorModel=/DeviceGray \
-dColorConversionStrategy=/Gray \
-dPDFUseOldCMS=false \
-o {nfile}_mono.pdf -f {nfile}.pdf"
        print(f"mono: {GSLINE}")
        os.system(GSLINE)

"""

make4ht - build system for TeX4ht
Usage:
make4ht [options] filename ["tex4ht.sty op." "tex4ht op." 
     "t4ht op" "latex op"]
-a,--loglevel (default status) Set log level.
            possible values: debug, info, status, warning, error, fatal
-b,--backend (default tex4ht) Backend used for xml generation.
     possible values: tex4ht or lua4ht
-c,--config (default xhtml) Custom config file
-d,--output-dir (default "")  Output directory
-e,--build-file (default nil)  If the build filename is different 
     than `filename`.mk4
-f,--format  (default nil)  Output file format
-j,--jobname (default nil)  Set the jobname
-l,--lua  Use lualatex for document compilation
-m,--mode (default default) Switch which can be used in the makefile
-n,--no-tex4ht  Disable DVI file processing with tex4ht command
-s,--shell-escape Enables running external programs from LaTeX
-u,--utf8  For output documents in utf8 encoding
-x,--xetex Use xelatex for document compilation
-v,--version  Print version number
<filename> (string) Input filename


: use mjcli to convert math in MathML or \LaTeX\ format to plain HTML + CSS.
MathML is used by default.
If you want to use \LaTeX\ math, add "mathjax" option on the command line
(like make4ht -f html5+mjcli filename.tex "mathjax").
See the available settings.

"""

def toxhtml(filename, cstr, ddir):
    """Compile with: pdflatex <filename>."""
    print(rf"filename: {filename}, ddir: {ddir}")
    print(rf"cstr: {cstr}")                        # to compile html
    os.system(cstr)
##    cstr = rf'make4ht -m clean {filename}' # to clean builds files
##    print(rf"cstr: {cstr}")
##    print("Cancello i file temporanei.")
##    os.system(cstr)

def clean(path):
    """Clean recursiveli the directory an sub dir."""
    with os.scandir(path) as it:
        for entry in it:
            if True : #not entry.name.startswith('.'):
                if entry.is_file():
                    name, ext = os.path.splitext(entry.name)
                    if ext in EXTCLEAR:
                        print(path, '-->', entry.name)
                        os.remove(entry)
                if entry.is_dir():
                    print(f"'dir:  ' {entry.name}")
                    if entry.name in SAFEDIR:
                        print('SALVATA!!!')
                    else:
                        clean(entry)

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, nfiles = getopt.getopt(argv,"hctxjmi:o:",["ifile=","ofile="])
##        print(opts, args)
    except(getopt.GetoptError):
        print(__doc__)
        sys.exit(2)
    ptest, pmono  = False, False
    if nfiles == []:
        nfiles = [n_f for n_f in os.listdir('.') if n_f.endswith('.tex')]
##    stop
##    print(opts)
    for opt, arg in opts:
        if opt == '-h':
            print(__doc__)
            sys.exit()
        elif opt == '-x':
            print("xhtml+mathml:")
            for filename in nfiles:
                toxhtml(filename,
                        rf'make4ht {filename} -l -u -s -d {DDIR} "mathml"',
                        DDIR)
            return
        elif opt == '-j':
            print("xhtml+mathjax:")
            for filename in nfiles:
                toxhtml(filename,
         rf'make4ht {filename} -c md_make4ht -l -u -s -d {DDIR} "mathjax"',
                        DDIR)
            return
        elif opt == '-c':
            print("Cancellati:")
            clean('.')
            return
        elif opt == '-t':
            ptest = True
        elif opt == '-m':
            pmono = True
##      elif opt in ("-i", "--ifile"):
##         inputfile = arg
##      elif opt in ("-o", "--ofile"):
##         outputfile = arg
##   print('Input file is "', inputfile)
##   print('Output file is "', outputfile)
    for filename in nfiles:
        topdf(filename, ptest, pmono)

##def topdf(filename, test):
##    """Compile with: pdflatex <filename>."""
##    nfile = filename[:-4]
##    print(nfile)
##    os.system('pdflatex --shell-escape ' + filename)
##    if not test:
##        os.system('pdflatex --shell-escape ' + filename)
##        os.system('make clean')
##        GSLINE = rf"gs -sDEVICE=pdfwrite \
##-dProcessColorModel=/DeviceGray \
##-dColorConversionStrategy=/Gray \
##-dPDFUseOldCMS=false \
##-o {nfile}_mono.pdf -f {nfile}.pdf"
##        os.system(GSLINE)

##def main(argv):
##    inputfile = ''
##    outputfile = ''
##    try:
##        opts, nfiles = getopt.getopt(argv,"hti:o:",["ifile=","ofile="])
####        print(opts, args)
##    except(getopt.GetoptError):
##        print(__doc__)
##        sys.exit(2)
##    ptest = False
##    for opt, arg in opts:
##        if opt == '-h':
##             print(__doc__)
##             sys.exit()
##        if opt == '-t':
##             ptest = True
####      elif opt in ("-i", "--ifile"):
####         inputfile = arg
####      elif opt in ("-o", "--ofile"):
####         outputfile = arg
####   print('Input file is "', inputfile)
####   print('Output file is "', outputfile)
##    if nfiles == []:
##        nfiles = [n_f for n_f in os.listdir('.') if n_f.endswith('.tex')]
##    for filename in nfiles:
##        topdf(filename, ptest)

if __name__ == "__main__":
    main(sys.argv[1:])

