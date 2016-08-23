# 20/08/2016 --- Perpendicolare --- Daniele Zambelli
"""
Disegna: una retta AB e un punto C
Costruisci la perpendicolare ad AB passante per C.
"""

# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: retta AB e punto C
p_a = pyig.Point(-5, -4, width=6, name="A")
p_b = pyig.Point(-1, -5, width=6, name="B")
r_ab = pyig.Line(p_a, p_b, color="dark green")
p_c = pyig.Point(4, -1, width=6, name="C")
## Costruzione dell'angolo di 60°
c_ab = pyig.Circle(p_c, p_b, width=1)      # circ di centro C passante per B
p_d = pyig.Intersection(c_ab, r_ab, -1, name="D")    # intersezione D
p_e = pyig.Intersection(c_ab, r_ab, +1, name="E")    # intersezione E
c_de = pyig.Circle(p_d, p_e, width=1)      # circ di centro B passante per C
c_ed = pyig.Circle(p_e, p_d, width=1)      # circ di centro D passante per C
p_f = pyig.Intersection(c_de, c_ed, -1, name="F")    # intersezione F
p_g = pyig.Intersection(c_de, c_ed, +1, name="G")    # intersezione G
pyig.Line(p_f, p_g, color="chocolate") # la perpendicolare cercata
## attivazione della finestra grafica
ip.mainloop()
