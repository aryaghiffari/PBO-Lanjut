class mahasiswa:
    def __init__(self, univ, anggota, kkm) -> None:
        self.univ = univ
        self.anggota = anggota
        self. kkm = kkm
        print("Kelompok KKM:",self.univ, self.anggota, self.kkm)

class kkm:
    def __init__(self) -> None:
        self.kelompok = []
    def add_kelompok(self, kelompok):
        self.kelompok.append(kelompok)
class kelompok_kkm:
    def __init__(self, kkm) -> None:
        self.kkm = kkm

kelom1 = mahasiswa ("UMC,", "Arya G dan Argy R,","KKM desa konoha")
kkm1= kkm()
kkm1.add_kelompok(kelom1)
kelom = kelompok_kkm(kkm1)
kelom.kkm.kelompok