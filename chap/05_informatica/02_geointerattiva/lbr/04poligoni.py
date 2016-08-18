# 18/08/2016 
# Daniele Zambelli
# Poligoni

"""
Problema:
Disegna:
- un triangolo nel primo quadrante,
- un quadrilatero nel secondo,
- un pentagono nel terzo,
- un esagono nel quarto.
"""

# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## triangolo
pyig.Ray(pyig.Point(2, 1, width=6, name="A"),
         pyig.Point(5, 7, width=6, name="B"))
## quadrilatero
pyig.Angle(pyig.Point(-2, 3, width=6, name="C"),
           pyig.Point(-8, 3, width=6, name="V_1"),
           pyig.Point(-4, 7, width=6, name="D"))
## pentagono
pyig.Angle(pyig.Point(-4, -7, width=6, name="E"),
           pyig.Point(-10, -3, width=6, name="V_2"),
           pyig.Point(-5, -3, width=6, name="F"), [0])
## esagono
pyig.Angle(pyig.Point(9, -2, width=6, name="G"),
           pyig.Point(4, -2, width=6, name="V_3"),
           pyig.Point(8, -5, width=6, name="H"), [0, 1])
## attivazione della finestra grafica
ip.mainloop()
