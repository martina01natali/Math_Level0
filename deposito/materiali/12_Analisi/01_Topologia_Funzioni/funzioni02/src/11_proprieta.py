grafico(lambda x: 2**(x+1))

grafico(lambda x: x**2 -2)

grafico(lambda x: x**3 -4*x)

grafico(lambda x: -np.exp(x))

grafico(lambda x: x**3+2)

grafico(lambda x: np.log2(x))

tabella(lambda x: np.log2(x), [x/2 for x in range(-10, 10)])

grafico(lambda x: -.5*x+2)

grafico(lambda x: (x**3 -3*x)/(-2*x**3 +5*x))

tabella(lambda x: (x**3 -3*x)/(-2*x**3 +5*x), range(-10, 0))
tabella(lambda x: (x**3 -3*x)/(-2*x**3 +5*x), range(1, 11))

grafico(lambda x: (x**3 - 6*x)/(x**2 + 4))

tabella(lambda x: (x**3 - 6*x)/(x**2 + 4), range(-10, 11))

grafico(lambda x: np.sin(x)+2*np.sin(2*x))
