"""
Quanti sono i numeri dispari formati da 4 cifre tutte diverse tra loro
(un numero di quattro cifre non può iniziare per 0,
altrimenti sarebbe di 3 cifre).
"""

def dispariconcifrediverse(numcifre):
    return [num for num in range(10**(numcifre-1), 10**numcifre)
            if (num % 2 == 1) and (len(set(str(num))) == numcifre)]

listanumeri = dispariconcifrediverse(4)
print(listanumeri)
print(len(listanumeri))
