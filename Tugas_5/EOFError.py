try:
     string = input()
     print(string)
except EOFError:
     print("tidak ada data yang dimasukan dalam fungsi input")

#Tidak Muncul kesalahan walaupun menekan enter
#karena mendaftarkan variabel dalam string
#dapat dipicu dengan input Ctrl+Z -> Enter