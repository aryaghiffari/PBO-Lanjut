class manusia:
    def __init__(self,nama) -> None:
        self.nama = nama
    def berbicara(self):
        print("Manusia dapat menulis dengan bahasanya masing2")
class guru(manusia):
    def __init__(self, nama, menulis) -> None:
        super().__init__(nama)
        self.menulis = menulis
    def berbicara(self):
        return super().berbicara()
class murid(guru):
    def __init__(self, nama,menulis, belajar) -> None:
        super().__init__(nama,menulis)
        self.belajar= belajar
    def berbicara(self):
        print(f"Murid sedang presentasi")
A=guru("Arya Ghiffari","Catatan")
A.berbicara()
B=murid("Nafisa","catatan", "PBO")
B.berbicara()