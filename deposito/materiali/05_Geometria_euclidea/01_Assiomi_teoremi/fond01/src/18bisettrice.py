# 19/08/2016 --- Bisettrice --- Daniele Zambelli
"""
Disegna: un angolo 
Costruisci la sua bisettrice.
"""
# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: angolo AVB
p_a = pyig.Point(1, -2, width=6, name="A")
p_v = pyig.Point(-4, 1, width=6, name="V")
p_b = pyig.Point(3, 4, width=6, name="B")
angolo = pyig.Angle(p_a, p_v, p_b, [0, 1], color="dark green")
## Costruzione della bisettrice
c_va = pyig.Circle(p_v, p_a, width=1)    # circ centro p_v passante per p_a
p_c = pyig.Intersection(angolo.side1(), c_va, +1, name="C") # lato1 - circ.
c_av = pyig.Circle(p_a, p_v, width=1)    # circ di centro A passante per V
c_cv = pyig.Circle(p_c, p_v, width=1)    # circ di centro C passante per V
p_d = pyig.Intersection(c_av, c_cv, -1)  # intersezione
pyig.Line(p_v, p_d, color="chocolate")   # bisettrice
p_e = pyig.Intersection(c_av, c_cv, +1)  # Queste due linee servono
pyig.Line(p_v, p_e, color="chocolate")   # se l'angolo e' ottuso
## attivazione della finestra grafica
ip.mainloop()
