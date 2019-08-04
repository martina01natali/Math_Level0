def duegrafici(f_0, f_1):
  """Traccia i grafici di due funzioni."""
  assi()
  x = np.arange(-20., 10.3, 0.1)
  plt.plot(x, f_0(x))
  plt.plot(x, f_1(x))
  plt.show()
  
duegrafici(lambda x: np.exp(x), lambda x: np.log(x))
