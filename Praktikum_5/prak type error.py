Mhs_kelas_A = ["Argy Rem","Shin sato","Rin"]
index = ["Chenzia"]
for i in range(len(index)):
	try:
		print(Mhs_kelas_A[index[i]])
	except TypeError:
		print("Bukan Mahasiswa Kelas A")
