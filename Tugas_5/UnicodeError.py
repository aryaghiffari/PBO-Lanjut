a= '\U0001f60a'
try:
    a.encode('ISO-8859-1')
except UnicodeError as e:
    print("Terjadi kesalahan encode / decode terkait unicode")