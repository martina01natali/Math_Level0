# 20/08/2016 --- Angolo di 60° --- Daniele Zambelli
"""
Disegna: una semiretta AB
Costruisci Un angolo di 60°.
"""

# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: retta AB e punto C
p_a = pyig.Point(-6, -3, width=6, name="A")
p_b = pyig.Point(-1, -5, width=6, name="B")
r_ab = pyig.Line(p_a, p_b, color="dark green")
p_c = pyig.Point(1, 2, width=6, name="C")
## Costruzione dell'angolo di 60°
c_ab = pyig.Circle(p_c, p_b, width=1)      # circ di centro C passante per B
p_d = pyig.Intersection(c_ab, r_ab, +1, name="D")    # intersezione D
##c_ba = pyig.Circle(p_b, p_a, width=1)      # circ di centro B passante per A
##c_ba = pyig.Circle(p_b, p_a, width=1)      # circ di centro B passante per A
##p_c = pyig.Intersection(c_ab, c_ba, +1, name="C")    # intersezione C
##p_d = pyig.Intersection(c_ab, c_ba, -1, name="D")    # intersezione D
## attivazione della finestra grafica
ip.mainloop()
