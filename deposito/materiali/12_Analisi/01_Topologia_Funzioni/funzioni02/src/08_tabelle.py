def tabella(f, argomenti):
  """Stampa in verticale argomento e risultato di f 
  per tutti i valori contenuti in argomenti"""
  print("x", "\t", "f(x)")
  for x in argomenti:
    print(x, "\t", f(x))
    
tabella(lambda x: x / 2 + 3, range(-5, +5))

def tabella_o(f, argomenti):
  """Stampa in orizzontale argomento e risultato di f 
  per tutti i valori contenuti in argomenti"""
  print("x:", end="\t")
  for x in argomenti:
    print(x, end="\t")
  print()
  print("f(x):", end="\t")
  for x in argomenti:
    print(f(x), end="\t")
  print()
   
tabella_o(lambda x: x / 2 + 3, range(-6, +7))
