try:
    a= '\U0001f60a'
    print(a)
    a.encode('ISO-8859-1')
except:
    print("Terdapat kesalahan encoding berkaitan Unicode")