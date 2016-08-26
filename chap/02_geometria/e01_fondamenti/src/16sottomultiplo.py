# 20/08/2016 --- Sottomultiplo --- Daniele Zambelli
"""
Disegna: un segmento AB
Costruisci il segmento AB'' congruente a un terzo di AB.
"""

# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: segmento AB
p_a = pyig.Point(-10, -3, width=6, name="A")
p_b = pyig.Point(7, 2, width=6, name="B")
s_ab = pyig.Segment(p_a, p_b, color="dark green")
## Costruzione di AD congruente a un terzo di AB
p_c = pyig.Point(-7, 1, width=6, name="C")
r_ac = pyig.Ray(p_a, p_c, width=1)
c_c_a = pyig.Circle(p_c, p_a, width=1)   # circ di centro C passante per A
p_c1 = pyig.Intersection(r_ac, c_c_a, +1, name="C'")    # intersezione C'
c_c1_c = pyig.Circle(p_c1, p_c, width=1) # circ di centro C' passante per C
p_c2 = pyig.Intersection(r_ac, c_c1_c, +1, name="C''")  # intersezione C'
r_c2b = pyig.Line(p_c2, p_b, width=1)       # retta C''B
r_c2b2 = pyig.Parallel(r_c2b, p_c, width=1) # retta parall. a C''B pass. C
p_d = pyig.Intersection(r_c2b2, s_ab, name="D")         # intersezione D
pyig.Segment(p_a, p_d, color="chocolate")   # AD e' il segmento richiesto
## attivazione della finestra grafica
ip.mainloop()
