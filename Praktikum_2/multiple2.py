class diri:
    def __init__(self, nama, umur) -> None:
        self.nama = nama
        self.umur = umur
    def get_info(self):
        print(f"Nama :{self.nama}")
        print(f"umur : {self.umur}")
class identitas :
    def __init__(self, ttl, hobi) -> None:
        self.ttl= ttl
        self.hobi = hobi
    def get_info(self):
        print(f"Tempat & tgl lahir{self.ttl}")
        print(f"Hobi : {self.hobi}")
class individu:
    def __init__(self, pekerjaan, ttl):
        self.pekerjaan = pekerjaan
        self.ttl = ttl
    def get_info(self):
        print(f"Pekerjaan : {self.pekerjaan}")
        print (f"Tempat & tgl lahir:{self.ttl}")
class aku(identitas,individu):
    def __init__(self, nama, umur, ttl, pekerjaan, hobi) -> None:
        diri.__init__(self, nama, umur)
        identitas.__init__(self, ttl,hobi)
        individu.__init__(self,pekerjaan, ttl)
    def get_info(self):
        super().get_info()
        print(f"Nama :{self.nama}")
        print(f"umur : {self.umur}")
        print(f"Tempat & tgl lahir:{self.ttl}")
        print(f"Hobi : {self.hobi}")
        print(f"Pekerjaan : {self.pekerjaan}")
datadiri= aku("Arya Ghiffari", 20, "Cirebon, 21-08-2002","Mahasiswa","Nonton Anime")
datadiri.get_info()