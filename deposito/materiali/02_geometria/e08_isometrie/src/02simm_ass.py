# 24/08/2016 --- Simmetria assiale --- Daniele Zambelli
"""
Disegna: Il punto P e l'asse doi simmetria k. 
Costruisci il punto P' simmetrico di P rispetto all'asse k.
"""
# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: Punto P e centro O
p_p = pyig.Point(-4, 6, width=6, name="P")
r_k = pyig.Line(pyig.Point(-2, -7, width=6), pyig.Point(4, 12, width=6),
                color="dark green", name="k")
## Costruzione del Simmetrico rispetto a O
r_orth = pyig.Orthogonal(r_k, p_p, width=1)    # retta per P perpend. a k
p_h = pyig.Intersection(r_k, r_orth)
c_op = pyig.Circle(p_h, p_p, width=1)   # circ di centro O passante per P
p_p1 = pyig.Intersection(c_op, r_orth, -1, width=6,
                         color="chocolate", name="P'") # P' cercato
## attivazione della finestra grafica
ip.mainloop()
