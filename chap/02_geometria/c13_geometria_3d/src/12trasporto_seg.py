# 19/08/2016 --- Trasporto di un segmento --- Daniele Zambelli
"""
Disegna: un punto A e un segmento BC
Costruisci la circonferenza di centro A e di raggio BC.
"""
# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: punto A e segmento BC
p_a = pyig.Point(-1, 3, width=6, name="A")
p_b = pyig.Point(4, 2, width=6, name="B")
p_c = pyig.Point(6, 1, width=6, name="C")
pyig.Segment(p_b, p_c, color="dark green")
## Costruzione della circoferenza di centro A e di raggio BC
c_ab = pyig.Circle(p_a, p_b, width=1)     # circ di centro A passante per B
c_ba = pyig.Circle(p_b, p_a, width=1)     # circ di centro B passante per A
p_d = pyig.Intersection(c_ab, c_ba, +1, name="D")   # intersezione
r_b = pyig.Ray(p_d, p_b, width=1)         # semiretta DB
r_a = pyig.Ray(p_d, p_a, width=1)         # semiretta DA
c_bc = pyig.Circle(p_b, p_c, width=1)     # circ di centro B passante per C
p_e = pyig.Intersection(r_b, c_bc, +1, name="E")   # intersezione E
c_de = pyig.Circle(p_d, p_e, width=1)     # circ di centro D passante per E
p_f = pyig.Intersection(r_a, c_de, +1, name="F")   # intersezione F
pyig.Circle(p_a, p_f, color="chocolate")  # Circonferenza richiesta
## attivazione della finestra grafica
ip.mainloop()
