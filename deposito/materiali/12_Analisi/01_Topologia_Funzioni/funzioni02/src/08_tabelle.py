def tabella(f, argomenti):
  """Stampa argomento e risultato di f 
  per tutti i valori contenuti in argomenti"""
  print("x", "\t", "f(x)")
  for x in argomenti:
    print(x, "\t", f(x))
    
tabella(f_0, range(-5, +5))

def tabella_o(f, argomenti):
  """Stampa argomento e risultato di f 
  per tutti i valori contenuti in argomenti"""
  print("x:", end="\t")
  for x in argomenti:
    print(x, end="\t")
  print()
  print("f(x):", end="\t")
  for x in argomenti:
    print(f(x), end="\t")
  print()
   
tabella_o(f_0, range(-6, +7))
