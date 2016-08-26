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
p_a = pyig.Point(-3, 2, width=6)
p_b = pyig.Point(-2, -5, width=6)
p_c = pyig.Point(7, -1, width=6)
triequi(p_a, p_b, width=4, color="DebianRed", intcolor="gold")
triequi(p_b, p_c, width=4, color="DebianRed", intcolor="gold")
triequi(p_c, p_a, width=4, color="DebianRed", intcolor="gold")
## attivazione della finestra grafica
ip.mainloop()
