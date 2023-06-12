class buku :
    def __init__(self, penulis, judul) -> None:
        self.penulis = penulis
        self.judul = judul
        print(self.judul, ",oleh :", self.penulis)
class penulis:
    def __init__(self) -> None:
        self.nama = []
    def add_nama(self, nama):
        self.nama.append(nama)
class karya:
    def __init__(self,penulis):
        self.penulis = penulis

buku1 = buku ("Arya Ghiffari","Mengetahui Rasi Bintang")
writer = penulis()
writer.add_nama(buku1)
create = karya(writer)
create.penulis.nama