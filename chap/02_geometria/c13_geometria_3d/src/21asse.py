# 21/08/2016 --- Asse --- Daniele Zambelli
"""
Disegna: due punti liberi e il segmento che li congiunge 
Costruisci l'asse del segmento.
"""
# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: segmento AB
p_a = pyig.Point(-1, 3, width=6, name="A")
p_b = pyig.Point(6, 1, width=6, name="B")
s_2 = pyig.Segment(p_a, p_b, color="dark green", width=6)
## Costruzione dell'asse
c_ab = pyig.Circle(p_a, p_b, width=1)   # circ di centro A passante per B
c_ba = pyig.Circle(p_b, p_a, width=1)   # circ di centro B passante per A
p_c = pyig.Intersection(c_ab, c_ba, +1, name="C")  # intersezione C
p_d = pyig.Intersection(c_ab, c_ba, -1, name="D")  # intersezione D
pyig.Line(p_c, p_d, color='chocolate') # asse
## attivazione della finestra grafica
ip.mainloop()
