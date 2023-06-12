try:
    data = "100" * (10**10)
    print(data)
except MemoryError:
    print("Memori tidak cukup untuk menampung data yang diminta!")