try:
    x = 10
    y = x / 0
    print(y)
except ZeroDivisionError:
    print("Terjadi kesalahan pembagian dengan nol!")