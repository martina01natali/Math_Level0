# 20/08/2016 --- Trasporto di un angolo --- Daniele Zambelli
"""
Disegna: un angolo AVB e una semiretta V'D
Costruisci sulla semiretta un angolo congruente a AVB.
"""
# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: punto A e segmento BC
p_a = pyig.Point(-1, 5, width=6, name="A")
p_v = pyig.Point(-10, 6, width=6, name="V")
p_b = pyig.Point(-5, 8, width=6, name="B")
a_0 = pyig.Angle(p_a, p_v, p_b, [0, 1], color="dark green")
p_v1 = pyig.Point(1, -8, width=6, name="V'")
p_d = pyig.Point(13, -9, width=6, name="D")
r_0 = pyig.Ray(p_v1, p_d, color="dark green")
## Costruzione dell'angolo congruente
c_va = pyig.Circle(p_v, p_a, width=1)       # circ di centro V passante per A
p_e = pyig.Intersection(a_0.side1(), c_va, +1, name="E")   # intersezione E
s_va = pyig.Segment(p_v, p_a, visible=False)# segmento VA
c_v1_va = pyig.Circle(p_v1, s_va, width=1)  # circ di centro V' di raggio VA
p_a1 = pyig.Intersection(r_0, c_v1_va, +1, name="A'")   # intersezione A'
s_ae = pyig.Segment(p_a, p_e, visible=False)# segmento AE
c_a1_ae = pyig.Circle(p_a1, s_ae, width=1)  # circ di centro V' e raggio AE
p_e1 = pyig.Intersection(c_v1_va, c_a1_ae, +1, name="E'")   # intersezione E'
a_1 = pyig.Angle(p_a1, p_v1, p_e1, [0, 1], color="chocolate") # ang. richiesto
## attivazione della finestra grafica
ip.mainloop()
