# 26/08/2016 --- Ettagono regolare --- Daniele Zambelli
"""
Disegnare un ettagono regolare.
"""
# lettura delle librerie
import pyig
#costanti
NUMLATI = 7
# programma principale
ip = pyig.InteractivePlane()
centro = pyig.Point(-3, 2, width=6, name="C")
p_p = pyig.Point(5, 3, width=6, name="P")
c_cp = pyig.Circle(centro, p_p, width=1)
arco = 2./ NUMLATI
vertici = [pyig.PointOn(c_cp, arco*cont, color="red")
                          for cont in range(NUMLATI)]
pyig.Polygon(vertici, intcolor="yellow")
## attivazione della finestra grafica
ip.mainloop()
