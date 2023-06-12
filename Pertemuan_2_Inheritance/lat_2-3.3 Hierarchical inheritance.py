class Kendaraan:
    def __init__(self, nama):
        self.nama = nama
    def get_nama(self):
        self.nama
        print(f"Nama : {self.nama}")
class Mobil(Kendaraan):
    def __init__(self, nama, merek):
        super().__init__(nama)
        self.merek = merek
    def get_merek(self):
        self.merek
        print(f"Merk : {self.merek}")
class SepedaMotor(Kendaraan):
    def __init__(self, nama, tipe):
        super().__init__(nama)
        self.tipe = tipe
    def get_tipe(self):
        self.tipe
        print(f"Type : {self.tipe}")
# turunan Hierarchical Inheritance
class Truk(Mobil):
    def __init__(self, nama, merek, kapasitas):
        super().__init__(nama, merek)
        self.kapasitas = kapasitas
    def get_kapasitas(self):
        self.kapasitas
        print(f"Kapasitas : {self.kapasitas}")
# turunan Hierarchical Inheritance
class MotorListrik(SepedaMotor):
    def __init__(self, nama, tipe, daya):
        super().__init__(nama, tipe)
        self.daya = daya
    def get_daya(self):
        self.daya
        print(f"daya : {self.daya}")
a=SepedaMotor("Aerox","R")
a.get_nama()
a.get_tipe()