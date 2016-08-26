# 17/08/2016 
# Daniele Zambelli
# Un piano vuoto

"""
Prova.
"""

# lettura delle librerie 
import pyig
# programma principale
ip = pyig.InteractivePlane('Orthogonal')

# Inizio esempio::

p_a = pyig.Point(-7, -3, color="#40c040", width=5, name="A")
p_b = pyig.Point(5, -5, color="#40c040", width=5, name="B")
p_c = pyig.Point(-3, 8, color="#40c040", width=5, name="C")
pyig.Polygon((p_a, p_b, p_c))      # Il triangolo
cba = pyig.Angle(p_c, p_b, p_a)  # Due angoli del triangolo
bac = pyig.Angle(p_b, p_a, p_c)
b1 = pyig.Bisector(cba, color="#a0c040") # Le bisettrici
b2 = pyig.Bisector(bac, color="#a0c040")
pyig.Intersection(b1, b2, color="#c040c0", width=5, name="Incentro")

# :: Fine esempio

## attivazione della finestra grafica
ip.mainloop()
