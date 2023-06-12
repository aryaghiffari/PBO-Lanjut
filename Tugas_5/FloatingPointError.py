import numpy as np
try:
  with np.errstate(invalid='raise'):
    print(np.sqrt(-1))
except FloatingPointError as e:
  print("Kesalahan floating")