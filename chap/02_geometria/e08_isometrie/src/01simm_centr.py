# 24/08/2016 --- Simmetria centrale --- Daniele Zambelli
"""
Disegna: Il punto P e il centro della simmetria O 
Costruisci il punto P' simmetrico di P rispetto ad O.
"""
# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: Punto P e centro O
p_p = pyig.Point(2, 5, width=6, name="P")
p_o = pyig.Point(5, 3, width=6, name="O")
## Costruzione del Simmetrico rispetto a O
r_op = pyig.Line(p_o, p_p, width=1)    # retta OP
c_op = pyig.Circle(p_o, p_p, width=1)   # circ di centro O passante per P
p_p1 = pyig.Intersection(c_op, r_op, -1, width=6,
                         color="chocolate", name="P'") # P' cercato
## attivazione della finestra grafica
ip.mainloop()
