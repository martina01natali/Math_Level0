# 17/08/2016 
# Daniele Zambelli
# Elementi di base della geometria interattiva

"""
Disegna: un punto nel primo quadrante, un segmento nel secondo,
una retta nel terzo, una circonferenza nel quarto.
"""

# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## punto
pyig.Point(3, 5, color="pink", width=6, name="A")
## segmento
p_1 = pyig.Point(-9, 6, width=6, name="B")
p_2 = pyig.Point(-2, 4, width=6, name="C")
pyig.Segment(p_1, p_2, color="red", width=4)
## retta
pyig.Line(pyig.Point(-3, -8, width=6, name="D"),
          pyig.Point(-8, -5, width=6, name="E"))
## circonferenza
pyig.Circle(pyig.Point(6, -5, width=6, name="Centro"),
            pyig.Point(7, -1, width=6, name="P"))
## attivazione della finestra grafica
ip.mainloop()
