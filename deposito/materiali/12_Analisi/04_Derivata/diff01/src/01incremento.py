# 19/08/2016 --- Calcolo dell'incremento di una funzione--- Daniele Zambelli
"""
Funzione che calcola l'incremento di una funzione.
"""
# Funzioni
def incremento(funzione, x_0, delta_x):
    return funzione(x_0 + delta_x) - funzione(x_0)

# programma principale
print(incremento(lambda x: 1/4*x**2-x-3, 3, 4))
print(incremento(lambda x: 1/4*x**2-x-3, 1, 4))
print(incremento(lambda x: 1/4*x**2-x-3, 1, 2))
