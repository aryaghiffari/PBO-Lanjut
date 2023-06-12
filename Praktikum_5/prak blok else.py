def pembagian(x, y):
	try:
		hasil = x // y
	except ZeroDivisionError:
		print("Tidak dapat dibagi dengan nol")
	else:
		print(hasil)
pembagian(45, 5)
