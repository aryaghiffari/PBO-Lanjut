class manusia:
    def __init__(self,nama) -> None:
        self.nama = nama
    def get_nama(self):
        self.nama
        print(f"Nama : {self.nama}")
class anak(manusia):
    def __init__(self, nama, jk ) -> None:
        super().__init__(nama)
        self.jk = jk
    def get_jk(self):
        self.jk
        print(f"Jenis Kelamin: {self.jk}")
class pelajar(manusia):
    def __init__(self, nama, pendidikan) -> None:
        super().__init__(nama)
        self.pendidikan= pendidikan
    def get_pendidikan(self):
        self.pendidikan
        print(f"Pendidikan Terakhir: {self.pendidikan}")
class individu(anak):
    def __init__(self, nama, jk, umur) -> None:
        super().__init__(nama, jk)
        self.umur = umur
    def get_umur(self):
        self.umur
        print(f"Usia : {self.umur}")
class alumni(pelajar):
    def __init__(self, nama, pendidikan, asal) -> None:
        super().__init__(nama, pendidikan)
        self.asal = asal
    def get_asal(self):
        self.asal
        print(f"Asal Perguruan : {self.asal}")
A= alumni("Arya Ghiffari", "S1 Teknik Informatika", "Universitas Muhammadiyahh Cirebon")
A.get_nama()
A.get_pendidikan()
A.get_asal()