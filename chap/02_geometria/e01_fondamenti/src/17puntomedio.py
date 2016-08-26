# 20/08/2016 --- Punto medio di un segmento --- Daniele Zambelli
"""
Disegna: un segmento AB
Costruisci il punto medio del segmento.
"""

# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: segmento AB
p_a = pyig.Point(-6, 3, width=6, name="A")
p_b = pyig.Point(2, 1, width=6, name="B")
s_ab = pyig.Segment(p_a, p_b, color="dark green")
## Costruzione del punto medio di AB
c_ab = pyig.Circle(p_a, p_b, width=1)      # circ di centro A passante per B
c_ba = pyig.Circle(p_b, p_a, width=1)      # circ di centro B passante per A
p_c = pyig.Intersection(c_ab, c_ba, +1, name="C")    # intersezione C
p_d = pyig.Intersection(c_ab, c_ba, -1, name="D")    # intersezione D
r_cd = pyig.Line(p_c, p_d, width=1)                  # retta CD
pyig.Intersection(r_cd, s_ab, name="M",
                  width=6, color="chocolate") # M e' il pto medio richiesto
## attivazione della finestra grafica
ip.mainloop()
