#!/usr/bin/python3
# -*- coding: utf-8 -*-
#-------------------------------python-------------------interi_esp.py--#
#                                                                       #
#                    Espressioni con numeri interi                      #
#                                                                       #
#--Daniele Zambelli--------------GPL------------------------------2021--#

"""
Calcola i valori delle seguenti espressioni.

"""

import random

def esegui(numes, listaespressioni):
    print(numes)
    for e in listaespressioni:
        print(fr" \hfill[{int(e)}]   {e}")
    print()

def randints(num, mi=-12, ma=+12):
    """Restituisce una sequenza di numneri interi cokmpresi tra mi e ma."""
    return (random.randint(mi, ma) for n in range(num))

def randops(num, operators):
    """Restituisce una sequenza di numneri interi cokmpresi tra mi e ma."""
    return (random.choice(operators) for n in range(num))

def crea_addsub(numop, mi=-12, ma=-12):
    """Crea una sequenza di addizioni e sottrazioni tra numeri interi."""
    operazioni = tuple(randops(numop, '-+')) + ('=',)
    operatori = randints(numop+1)
    espseq = (f'({num:+}) {op}' for num, op in zip(operatori, operazioni))
    espstr = ' '.join(espseq)
    ris = eval(espstr[:-1])
    return(rf"""\({espstr}\)
\hfill [\({ris}\)]""") 
    
crea_addsub(4)

def crea_addsubese(num):
    """Crea un esercizio con addizioni e sottrazioni nei num. interi."""
    eseini = r"""
\begin{esercizio}
Trasforma in somme algebriche, e poi calcola, le seguenti espressioni.
 \label{ese:as}
% \vspace{-1em}
% \begin{multicols}{2}
 \begin{enumerate}[noitemsep, label=(\alph*)]"""
    eseend = r"""\end{enumerate}
%\end{multicols}
\end{esercizio}

"""
    liststring = []
    liststring.append(eseini)
    for _ in range(num):
        liststring.append(rf'\item {crea_addsub(4+random.randrange(4))}')
    liststring.append(eseend)
    retstring = '\n'.join(liststring)
    
    return retstring

print(crea_addsubese(20))

pippo

  
esegui("es. 38",
       [(+5-2-1)+(+2+4+6),
        (-5+7-9)+(+1-2+3)-(+4-6+8),
        +4-3-(+2-1-(8-3)-(-5-2))-(2+3),
        -2+(-5+1)+(-7+4)-2 * (-6+1),
        15-9 * (-14+12)+8 * (-3+6)+ 5 * (-3+1)]
       )

esegui("es. 39",
       [(50-36-25)* (-15+5+20)-10* (-3-7),
        (+3-(10-5+25))* (-16+5-(-2-14))/(9+6),
        20/(+15-5)-30/(-10+5)+40/(15-20),
        18/(-3)+6* (1-5* (-2+4)+3)/ (-6)]
       )

esegui("es. 40",
       [100/2+3**2 -2**2* 6,
        2**7/2**3 -2**2,
        30-5* 3 -7* 2**2 -2,
        (3**2 +4**2) -(-3-4)**2,
        5* 5**3* 5**4/  (5**2 )**3 +5,
        32**5/16**4 +(-2)**9,
        (3**4* 3**3/3**6 )**2 +(7**2-5**2)/2**2,
        (3* 2**2 -10 )**4* (3**3+2**3)/7-10* 2**3]
       )

esegui("es. 41",
       [-5* (12-3+4)-2* (3-16/(-2+4))**2,
        (-3+(-5)* (-1))**3+(-4-(1-2))**2,
        (2* (-3)**2+2* (-3)* (-2))**2/(2**4-3*(+6))**2,
        (3* (-1)**2-3* (-3)* (-3))**3/(2**2+5* (-2)**2)**3]
       )

esegui("es. 42",
       [(-3)**2* (4-1)**5/((-4)**3/(2**5)-3**3/(-3)**3),
        (-(-2)* 2+(-10)**2/(-5)**2)* (3-5+2* (-3)**2-5),
        13-3-4* (-2)**2-5**3/5**2+3* (2**3-3**2)-6/(-3)-(4-7+3)**4,
        -1-3* (-3)**2-4**3/4**2+(-3-3)* (2**2+3**2)-(-12)/(-3)]
       )

esegui("es. 43",
       [(10-6* (-2)**2)/(-7)+(3**2/3)* 2**3-15/(-3)+((-3)**3/(-3)**0),
        abs(-5+8)-abs(-11)+(-abs(+4)* abs(-2* (+5)))**2,
        (-29+37)**5* (-5+abs(23-28))**7,
        -2* (-2* abs(-2))**2- (abs(3-5)* (3-5) )**2* (-2),
        (-1)**3* (-1* abs(-1))**2-(abs(-3-2)* (-5+3))**2* (-2+1)**3]
       )

