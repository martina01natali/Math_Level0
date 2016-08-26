# 20/08/2016 --- Parallela --- Daniele Zambelli
"""
Disegna: una retta AB e un punto A'
Costruisci la retta A'B' parallela alla retta AB.
"""
# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: retta AB e punto A'
p_a = pyig.Point(-10, 3, width=6, name="A")
p_b = pyig.Point(-1, 2, width=6, name="B")
r_ab = pyig.Line(p_a, p_b, color="dark green")
p_a1 = pyig.Point(-7, -3, width=6, name="A'")
## Costruzione della retta A'B' parallela ad AB
s_ab = pyig.Segment(p_a, p_b, visible=False)
c_a1_ab = pyig.Circle(p_a1, s_ab, width=1)   # circ di centro A1 e raggio AB
s_aa1 = pyig.Segment(p_a, p_a1, visible=False)
c_b_ab = pyig.Circle(p_b, s_aa1, width=1)   # circ di centro B e raggio AA'
p_b1 = pyig.Intersection(c_a1_ab, c_b_ab, -1, name="B'")    # intersezione B'
r_a1b1 = pyig.Line(p_a1, p_b1, color="chocolate") # retta parallela
# La procedura funziona solo se A' si trova da una certa parte della retta AB
# Se A' si trova dall'altra parte si deve scegliere l'atra intersezione
## attivazione della finestra grafica
ip.mainloop()
