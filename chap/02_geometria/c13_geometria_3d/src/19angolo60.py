# 20/08/2016 --- Angolo di 60° --- Daniele Zambelli
"""
Disegna: una semiretta AB
Costruisci Un angolo di 60°.
"""

# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## Dati: semiretta AB
p_a = pyig.Point(-6, 3, width=6, name="A")
p_b = pyig.Point(-1, 1, width=6, name="B")
r_ab = pyig.Ray(p_a, p_b, color="dark green")
## Costruzione dell'angolo di 60°
c_ab = pyig.Circle(p_a, p_b, width=1)      # circ di centro A passante per B
c_ba = pyig.Circle(p_b, p_a, width=1)      # circ di centro B passante per A
p_c = pyig.Intersection(c_ab, c_ba, +1, name="C")    # intersezione C
p_d = pyig.Intersection(c_ab, c_ba, -1, name="D")    # intersezione D
angolo_60 = pyig.Angle(p_b, p_a, p_c, [0, 1],
                       color="chocolate") # BAC e' l'angolo richiesto
angolo_60 = pyig.Angle(p_c, p_a, p_d, [0, 1], width=1, 
                       color="chocolate") # CAD altro angolo notevole
angolo_60 = pyig.Angle(p_a, p_c, p_d, [0, 1], width=1, 
                       color="chocolate") # ACD altro angolo notevole
## attivazione della finestra grafica
ip.mainloop()
