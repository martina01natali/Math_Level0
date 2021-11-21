#!/usr/bin/python3
# -*- coding: utf-8 -*-
#-------------------------------python---------------interi_tabelle.py--#
#                                                                       #
#               Tabelle per esercizi sui numeri interi                  #
#                                                                       #
#--Daniele Zambelli--------------GPL------------------------------2021--#

"""
Costruisce alcune tabelle da riempire.

"""
def py2latex(espstr):
    """Restituisce una stringa aggiustata per LaTeX."""
    for old, new in (('+0', '~~~0'), (' * ', r' \cdot '), ('/', ':'),
                     (' ** ', '^')):
        espstr = espstr.replace(old, new)
    return espstr

def tabella1(valori, espressioni):
    """Crea una tabella calcolando 4 espressioni in base
a 1 valore assegnato."""
    esp0, esp1, esp2, esp3, esp4 = espressioni
    ese2ini = rf"""
\begin{{esercizio}}
 \label{{ese:tab1}}
Completa la seguente tabella.
\begin{{center}}
\begin{{tabular}}{{|m{{0.045\textwidth}}
                |m{{0.153\textwidth}}|m{{0.153\textwidth}}|m{{0.153\textwidth}}
                |m{{0.153\textwidth}}|m{{0.153\textwidth}}|}}
\hline
\(~~a\) & \(\quad {esp0}\) & \(\quad {esp1}\) & 
\(\quad {esp2}\) & \(\quad {esp3}\) & \(\quad {esp4}\) \\
\hline
"""
    ese2end = """\end{tabular}
\end{center}
\end{esercizio}

"""
    liststring = []
    liststring.append(ese2ini)
    for a in valori:
        liststring.append(fr"\rb{{{a:+}}}")
        for e in espressioni:
            liststring.append(fr" & \prb{{{eval(e):+}}} ")
        liststring.append("\n\\\\[1em] \\hline\n")
    liststring.append(ese2end)
    retstring = ''.join(liststring)
    return py2latex(retstring)

def tabella2(valori, espressioni):
    """Crea una tabella calcolando 4 espressioni in base
a 2 valori assegnati."""
    esp0, esp1, esp2, esp3 = espressioni
    ese2ini = rf"""
\begin{{esercizio}}
 \label{{ese:tab2}}
Completa la seguente tabella.
\begin{{center}}
\begin{{tabular}}{{|m{{0.045\textwidth}}|m{{0.045\textwidth}}
                |m{{0.18\textwidth}}|m{{0.18\textwidth}}
                |m{{0.18\textwidth}}|m{{0.18\textwidth}}|}}
\hline
\(~~a\) & \(~~b\) & \(\quad {esp0}\) & \(\quad {esp1}\) & 
\(\quad {esp2}\) & \(\quad {esp3}\) \\
\hline
"""
    ese2end = """\end{tabular}
\end{center}
\end{esercizio}

"""
    liststring = []
    liststring.append(ese2ini)
    for a, b in valori:
        liststring.append(fr"\rb{{{a:+}}} & \rb{{{b:+}}}")
        for e in espressioni:
            liststring.append(fr" & \prb{{{eval(e):+}}} ")
        liststring.append("\n\\\\[1em] \\hline\n")
    liststring.append(ese2end)
    retstring = ''.join(liststring)
    return py2latex(retstring)

def tabella3(valori, espressioni):
    """Crea una tabella calcolando 4 espressioni in base
a 3 valori assegnati."""
    esp0, esp1, esp2, esp3 = espressioni
    ese2ini = rf"""
\begin{{esercizio}}
 \label{{ese:tab3}}
Completa la seguente tabella.
\begin{{center}}
\begin{{tabular}}{{|m{{0.045\textwidth}}|m{{0.045\textwidth}}|m{{0.045\textwidth}}
                |m{{0.16\textwidth}}|m{{0.16\textwidth}}
                |m{{0.16\textwidth}}|m{{0.16\textwidth}}|}}
\hline
\(~~a\) & \(~~b\) & \(~~c\) & \(\quad {esp0}\) & \(\quad {esp1}\) & 
\(\quad {esp2}\) & \(\quad {esp3}\) \\
\hline
"""
    ese2end = """\end{tabular}
\end{center}
\end{esercizio}

"""
    liststring = []
    liststring.append(ese2ini)
    for a, b, c in valori:
        liststring.append(fr"\rb{{{a:+}}} & \rb{{{b:+}}} & \rb{{{c:+}}}")
        for e in espressioni:
            liststring.append(fr" & \prb{{{eval(e):+}}} ")
        liststring.append("\n\\\\[1em] \\hline\n")
    liststring.append(ese2end)
    retstring = ''.join(liststring)
    return py2latex(retstring)

print(tabella2(((-1, +2), (+2, +3), (+1, 0), (-2, -3), (+3, -3), (-10, +4)),
         ('a-b', '+a-b', '-a+b', '-a-b')))

print(tabella2(((-8, +2), (+6, +3), (+7, -4), (-5, -9), (+2, 0), (-8, +6)),
         ('a-b', '-(a-b)', '-a+b', '-a-(-b)')))

print(tabella3(((-1, +2, -3), (+2, +3, -5), (+1, 0, -1),
                (-5, -3, +4), (+7, -7, +7), (-11, 0, +4)),
         ('a-b+c', '(a-b)+c', 'a+(-b+c)', 'a-(+b+c)')))

print(tabella2(((-7, +2), (+5, +1), (+6, -3), (-4, -2), (0, -4), (-2, +8)),
         ('(a + b) * (a - b)', '(a + b) * (a + b)',
          '(a - b) * (a - b)', '(a + b) * (-a + b)')))

print(tabella2(((-24, +2), (+18, +1), (+48, -3),
                (-18, -9), (0, -4), (-36, +12)),
         ('a / b', '-a / b', '-(a / b)', 'a / -(b)')))

print(tabella2(((-7, +2), (+5, +1), (+6, -3), (-8, -9), (0, -4), (-10, +12)),
         ('a * b', '-a * b', '(-a) * (-b)', '-(a * b)')))

print(tabella2(((-7, +2), (-3, 4), (-3, 3), (-8, -2), (1, 5), (-10, +4)),
         ('a ** b', '(-a) ** b', '(+a) ** (-b)', '(-a) ** (-b)')))

print(tabella2(((-7, +2), (-3, 4), (-3, 3), (-8, -2), (1, 5), (-10, +4)),
         ('(a + b) ** 2', '(-a + b) ** 2', '(+a - b) ** 2', '(-a - b) ** 2')))

print(tabella1((-2, -1, 0, 1, 2, 3),
         ('a ** 2', '(-a) ** 2', '-a ** 2', 'a ** 3', '(-a) ** 3')))

print(tabella3(((-1, +2, -3), (+2, +3, -5), (+1, 0, -1),
                (-5, -3, +4), (+7, -7, +7), (-11, 0, +4)),
         ('-2 * a-b+c', '-2 * a-(b+c)', '-a-2 * b+c', 'a-b-2 * c')))

