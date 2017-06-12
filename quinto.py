#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------python----------------------creapdf.py--#
#                                                                       #
#                           da LaTeX a pdf                              #
#                                                                       #
#--Daniele Zambelli--------------GPL------------------------------2016--#

"""
Manda in compilazione latex il file quinto.tex

"""
from __future__ import division, print_function

import sys, getopt
import os

def main():
    """Compile with: pdflatex <filename>."""
    filename = "m_d_licei_17_5.tex"
    os.system('pdflatex --shell-escape ' + filename)
    os.system('pdflatex --shell-escape ' + filename)
    os.system('make clean')

if __name__ == "__main__":
    main()

