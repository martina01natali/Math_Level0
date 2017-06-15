# 19/08/2016 --- Triangolo isoscele dato il lato--- Daniele Zambelli
"""
Disegna: un segmento 
Costruisci i triangoli isosceli che abbiano quel segmento come lato obliquo.
"""
# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: segmento AB
p_a = pyig.Point(-1, 3, width=6, name="A")
p_b = pyig.Point(7, 1, width=6, name="B")
s_ab = pyig.Segment(p_a, p_b, width=5, color="dark green")
## Costruzione del triangolo
c_ab = pyig.Circle(p_a, p_b, width=1)  # circ. centro A passante per B
p_c = pyig.ConstrainedPoint(c_ab, .5, width=6, name="C") # vertice C
pyig.Polygon((p_a, p_b, p_c), color="chocolate", intcolor="gold") # triiso
## attivazione della finestra grafica
ip.mainloop()

