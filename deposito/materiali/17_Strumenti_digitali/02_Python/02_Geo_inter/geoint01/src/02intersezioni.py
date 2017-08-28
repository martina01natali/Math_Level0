# 18/08/2016 
# Daniele Zambelli
# Intersezioni

"""
Disegna:
- la retta r, passante per (-2; 7) e (5; 7);
- la circonferenza c, di centro (2; -5) e passante per (4; 0);
- la retta s, passante per (-3; 2) e (4; 2);
- l'intersezione tra le due rette s e r;
- l'intersezione tra la retta s e la circonferenza c.
"""

# lettura delle librerie 
import pyig

# programma principale
ip = pyig.InteractivePlane()
## retta r
retta_r = pyig.Line(pyig.Point(-2, 7, visible=False),
                    pyig.Point(5, 7, visible=False), name="r")
## circonferenza c
circ_c = pyig.Circle(pyig.Point(2, -5, visible=False),
                     pyig.Point(4, 0, visible=False), name="c")
## retta s
retta_s = pyig.Line(pyig.Point(-3, 2, width=6, name="A"),
                    pyig.Point(4, 2, width=6, name="B"), name="r")
## intersezione retta_s-retta_r
pyig.Intersection(retta_s, retta_r, color="green")
## intersezioni retta_s-circ_c
pyig.Intersection(retta_s, circ_c, -1, color="red")
pyig.Intersection(retta_s, circ_c, +1, color="yellow")
## attivazione della finestra grafica
ip.mainloop()
