try:
    i=1
    def penjumlahan():
        i = i+1
        print(i)
    penjumlahan()
except UnboundLocalError as e:
    print("Unbound Local Error!")