# 19/08/2016 
# Daniele Zambelli
# Poligoni

"""
Disegna: un triangolo nel primo quadrante, un quadrilatero nel secondo,
un pentagono nel terzo, un esagono nel quarto.
"""

# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## triangolo
p_0 = pyig.Point(2, 3, width=6, color="pale turquoise")
p_1 = pyig.Point(5, 1, width=6, color="cornflower blue")
p_2 = pyig.Point(7, 9, width=6, color="royal blue")
s_0 = pyig.Segment(p_0, p_1, color="indian red", width=6)
s_1 = pyig.Segment(p_1, p_2, color="salmon", width=6)
s_2 = pyig.Segment(p_2, p_0, color="rosy brown", width=6)
## quadrilatero
p_0 = pyig.Point(-2, 2, width=6)
p_1 = pyig.Point(-2, 8, width=6)
p_2 = pyig.Point(-8, 8, width=6)
p_3 = pyig.Point(-8, 2, width=6)
pyig.Polygon([p_0, p_1, p_2, p_3],
             width=6, color="dark green", intcolor="light steel blue")
## pentagono
vertici_p = [pyig.Point(-1, -2, width=6), pyig.Point(-6, -3, width=6),
             pyig.Point(-8, -5, width=6), pyig.Point(-7, -9, width=6),
             pyig.Point(-4, -5, width=6)]
pyig.Polygon(vertici_p, width=6, color="chocolate", intcolor="gold")
## esagono
coord = [(1, -3), (2, -5), (5, -7), (7, -8), (4, -4), (8, -2)]
vertici_e = [pyig.Point(x, y, width=6, color="pink") for x, y in coord]
pyig.Polygon(vertici_e, width=6, color="navy", intcolor="azure2")
## attivazione della finestra grafica
ip.mainloop()
