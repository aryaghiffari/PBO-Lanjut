def pembagian(x, y):
	try:
		hasil = x // y
		print("Hasil = ", hasil)
	except ZeroDivisionError:
		print("Tidak dapat dibagi dengan nol")
pembagian(45, 0)
