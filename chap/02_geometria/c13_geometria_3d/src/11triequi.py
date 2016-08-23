# 19/08/2016 --- Triangolo equilatero --- Daniele Zambelli
"""
Disegna: due punti liberi 
poi costruisci il punto medio tra i due.
"""
# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: punti A e B
p_a = pyig.Point(-1, 3, width=6, name="A")
p_b = pyig.Point(7, 1, width=6, name="B")
## Costruzione del triangolo equilatero
c_ab = pyig.Circle(p_a, p_b, width=1)   # circ di centro A passante per B
c_ba = pyig.Circle(p_b, p_a, width=1)   # circ di centro B passante per A
p_c = pyig.Intersection(c_ab, c_ba, +1, width=6, name="C")   # intersezione
pyig.Polygon((p_a, p_b, p_c), color="chocolate", intcolor="gold") # tri. eq.
## attivazione della finestra grafica
ip.mainloop()
