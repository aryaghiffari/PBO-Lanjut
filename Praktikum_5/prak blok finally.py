def pembagian(x, y):
	try:
		hasil = x // y
		print("Hasil = ", hasil)
	except ZeroDivisionError:
		print("Tidak dapat dibagi dengan nol")
	finally:
		print("program selesai dijalankan")
pembagian(45, 4)
