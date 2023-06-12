class Peneliti:
    def __init__(self, nama, judul):
        self.nama = nama
        self.judul = judul
class Jurnal:
    def __init__(self,nama, peneliti) -> None:
        self.nama = nama
        self.peneliti= peneliti
    def judul_jurnal(self):
        for peneliti in self.peneliti:
            print(peneliti.nama, peneliti.judul)
penelitiA = Peneliti("Arya Ghiffari :", "Kehidupan di planet Pluto")
penelitiB = Peneliti("Nafisa Nurul J :", "Kekuatan kucing dalam menegakan keadilan")
judul = Jurnal("Jurnal harian",[penelitiA, penelitiB])
judul.judul_jurnal()
        