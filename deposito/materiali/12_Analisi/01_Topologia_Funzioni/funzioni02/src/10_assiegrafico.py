import matplotlib.pyplot as plt
import numpy as np

def assi():
  """Traccia un piano cartesiano."""
  ax = plt.axes()
  ax.set(xlim=[-10.3,10.3],ylim=[-10.3,10.3], facecolor='white',
         xticks=range(-10, 11),yticks=range(-10, 11),
         xticklabels=[], yticklabels=[], aspect='equal')
  ax.grid(True, color='40')
  plt.arrow(-10.3,0,21,0, fc='w', ec='k', lw = .5, 
             head_width=.5, head_length=.5, overhang = .3, 
             length_includes_head = True, clip_on = False)
  plt.arrow(0,-10.3,0,21, fc='w', ec='k', lw = .5, 
             head_width=.5, head_length=.5, overhang = .3, 
             length_includes_head = True, clip_on = False)
  ax.text(10,-.7,'$x$')
  ax.text(-.8,10,'$y$')

def grafico(funzione):
  """Traccia il grafico di una funzione."""
  assi()
  x = np.arange(-20., 10.3, 0.1)
  plt.plot(x, funzione(x))
  plt.show()
  
grafico(lambda x: x**2-3)
grafico(lambda x: -x**2+4)
