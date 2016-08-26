# 20/08/2016 --- Multiplo di un segmento --- Daniele Zambelli
"""
Disegna: un segmento AB e la semiretta AB
Costruisci sulla semiretta il segmento AB'' uguale al triplo di AB.
"""
# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: punto A e semiretta AB
p_a = pyig.Point(-10, 3, width=6, name="A")
p_b = pyig.Point(-7, 2, width=6, name="B")
s_ab = pyig.Segment(p_a, p_b, width=6, color="dark green") # segmento AB
r_0 = pyig.Ray(p_a, p_b, color="dark green")
## Costruzione del segmento AB'' triplo di AB
c_1 = pyig.Circle(p_b, p_a, width=1)   # circ di centro B passante per A
p_b1 = pyig.Intersection(s_ab, c_1, +1, name="B'")    # intersezione B'
c_2 = pyig.Circle(p_b1, s_ab, width=1)  # circ di centro B' passante per B
p_b2 = pyig.Intersection(s_ab, c_2, +1, name="B''")   # intersezione B''
s_va = pyig.Segment(p_a, p_b2, color="chocolate")     # segmento richiesto
## attivazione della finestra grafica
ip.mainloop()
