class Univ:
    def __init__(self, nama, th) -> None:
        self.nama = nama
        self.th = th
    def get_info(self):
        print(f"Nama Univ: {self.nama}")
        print(f"Tahun Berdiri : {self.th}")
class fakultas(Univ):
    def __init__(self, nama, th, nf) -> None:
        super().__init__(nama, th)
        self.nf=nf
    def get_info(self):
        super().get_info()
        print(f"Nama Fakultas :{self.nf}")
class prodi(fakultas):
    def __init__(self, nama, th, nf, prodi) -> None:
        super().__init__(nama, th, nf)
        self.prodi=prodi
    def get_info(self):
        super().get_info()
        print(f"Teknik Informatika, Teknik Industri & Teknik Peternakan")

A= prodi("UMC", 2000, "Macdor", "a")
A.get_info()