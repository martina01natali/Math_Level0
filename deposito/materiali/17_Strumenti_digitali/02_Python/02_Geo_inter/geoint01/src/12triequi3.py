# 25/08/2016 --- Triangolo di triangoli --- Daniele Zambelli
"""
Disegnare un triangolo con un triangolo equilatero
costruito esternamente ad ogni lato
"""
# lettura delle librerie
import pyig

# funzioni
def triequi(p_0, p_1, **kargs):
    """Funzione che crea e restituisce un triangolo equilatero."""
    c_01 = pyig.Circle(p_0, p_1, visible=False)
    c_10 = pyig.Circle(p_1, p_0, visible=False)
    p_2 = pyig.Intersection(c_01, c_10, -1)
    return pyig.Polygon((p_0, p_1, p_2), **kargs)

# programma principale
ip = pyig.InteractivePlane()
vertici = ((-3, 2), (-2, -5), (7, -1))
p_a, p_b, p_c = (pyig.Point(x, y, width=6) for x, y in vertici)
for p_0, p_1 in ((p_a, p_b), (p_b, p_c), (p_c, p_a)): 
    triequi(p_0, p_1, width=4, color="DebianRed", intcolor="gold")
## attivazione della finestra grafica
ip.mainloop()
