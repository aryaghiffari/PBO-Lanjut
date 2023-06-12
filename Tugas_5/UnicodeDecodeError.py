try:
    "\x81".encode('ISO-8859-1').decode("utf-8")
except UnicodeDecodeError :
    print("Kesalahan Decoding terkait Unicode")