import math
try:
    print("Menghitung nilai eksponensial :")
    print(math.exp(999))
except OverflowError:
    print("Perhitungan melebihi batas MAXIMUM")