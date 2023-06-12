class manusia:
    def __init__(self, nama, umur) -> None:
        self.nama = nama
        self.umur = umur
    def get_name(self):
        self.nama
        print(f"Nama : {self.nama}")
    def get_umur(self):
        self.umur
        print(f"Umur : {self.umur}")
class petani(manusia):
    def __init__(self, nama, umur, tujuan) -> None:
        super().__init__(nama, umur)
        self.tujuan = tujuan
    def get_tujuan(self):
        self.tujuan
        print(f"Tujuan : {self.tujuan}")
class farm(petani):
    def __init__(self, nama, umur, tujuan, tanaman) -> None:
        super().__init__(nama, umur, tujuan)
        self.tanaman = tanaman
    def get_tanaman(self):
        self.tanaman
        print(f"Menanam: {self.tanaman}")

obj= farm("Rin",20,"menanam","padi")
obj.get_name()
obj.get_umur()
obj.get_tujuan()
obj.get_tanaman()