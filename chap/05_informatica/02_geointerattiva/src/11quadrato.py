# 24/08/2016 --- Quadrato --- Daniele Zambelli
"""
Dati: i punti A e B,
disegna il quadrato di lato AB.
"""
# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: punti A e B
p_a = pyig.Point(-5, -4, width=6, name="A")
p_b = pyig.Point(-1, -5, width=6, name="B")
## Costruzione del quadrato di lato AB
r_ab = pyig.Line(p_a, p_b, width=1)        # retta AB
r_ad = pyig.Orthogonal(r_ab, p_a, width=1) # perpend. a AB pass. per A
c_ab = pyig.Circle(p_a, p_b, width=1)      # circ. centro A pass. per B
p_d = pyig.Intersection(c_ab, r_ad, -1, name="D") # intersezione D
r_bc = pyig.Orthogonal(r_ab, p_b, width=1) # perpend. a AB pass. per B
r_dc = pyig.Orthogonal(r_ad, p_d, width=1) # perpend. a AD pass. per D
p_c = pyig.Intersection(r_dc, r_bc, name="C") # intersezione C
pyig.Polygon((p_a, p_b, p_c, p_d), color="chocolate", intcolor="gold")
## attivazione della finestra grafica
ip.mainloop()
