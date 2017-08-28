# 24/08/2016 --- Traslazione --- Daniele Zambelli
"""
Disegna: Il punto P e il vettore v. 
Costruisci il punto P' traslato di P di vettore v.
"""
# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: Punto P e centro O
p_p = pyig.Point(-4, 6, width=6, name="P")
s_v = pyig.Vector(pyig.Point(-11, 13, width=6), pyig.Point(-2, 11, width=6),
                color="dark green", name="v")
## Costruzione del Simmetrico rispetto a O
r_par = pyig.Parallel(s_v, p_p, width=1)   # retta per P parallela a v
c_ov = pyig.Circle(p_p, s_v, width=1)      # circ di centro O e raggio v
p_p1 = pyig.Intersection(c_ov, r_par, +1, width=6,
                         color="chocolate", name="P'") # P' cercato
## attivazione della finestra grafica
ip.mainloop()
