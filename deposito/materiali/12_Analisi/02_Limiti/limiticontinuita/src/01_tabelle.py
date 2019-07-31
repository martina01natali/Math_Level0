def tabella(f, argomenti):
  """Stampa argomento e risultato di f 
  per tutti i valori contenuti in argomenti"""
  print(r"""\begin{tabular}{r|r}
x & y\\\hline""")
  for x in argomenti:
##    print(x, f(x), sep=" & ", end=r"\\")
    print(rf"{x} & {f(x)} \\")
  print("\end{tabular}\n")

def f_0(x):
  return (x**2-6*x+5)/(x**2+2*x-3)

tabella(f_0, (-100, -1000, -10000))
tabella(f_0, (-2.9, -2.99, -2.999, -3.001, -3.01, -3.1))
tabella(f_0, (0.9, 0.99, 0.999, 1.001, 1.01, 1.1))
tabella(f_0, (100, 1000, 10000))

def f_1(x):
  return 2*x - (4*x**2 -8*x +3)**.5

tabella(f_1, (100, 1000, 10000))

##def tabella_o(f, argomenti):
##  """Stampa argomento e risultato di f 
##  per tutti i valori contenuti in argomenti"""
##  print("x:", end="\t")
##  for x in argomenti:
##    print(x, end="\t")
##  print()
##  print("f(x):", end="\t")
##  for x in argomenti:
##    print(f(x), end="\t")
##  print()
##   
##tabella_o(f_0, range(-6, +7))
