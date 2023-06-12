from abc import ABCMeta, abstractmethod, abstractstaticmethod

class Universitas(metaclass = ABCMeta):
    @abstractmethod
    def __init__(self, mhs) -> None:
        """ implement in child class """

    @abstractstaticmethod
    def print_Universitas():
        """ implement in child class """

class Informatika(Universitas):
    def __init__(self, mhs) -> None:
        self.mhs = mhs
    
    def print_Universitas(self):
        print(f"Mahasiswa Teknik Informatika : {self.mhs}")

class Industri(Universitas):
    def __init__(self, mhs) -> None:
        self.mhs = mhs
    
    def print_Universitas(self):
        print(f"Mahasiswa Teknik Industri : {self.mhs}")

class ParentUniv(Universitas):
    def __init__(self, mhs) -> None:
        self.mhs = mhs
        self.base_mhs = mhs
        self.sub_mhs = []

    def add(self, dept):
        self.sub_mhs.append(dept)
        self.mhs += dept.mhs

    def print_Universitas(self):
        print("Jumlah Civitas Akademik Fakultas Teknik ErrorUniversity")
        print(f"Dosen: {self.base_mhs}")
        for dept in self.sub_mhs:
            dept.print_Universitas()
        print(f"Total Civitas : {self.mhs}")

mhs1 = Informatika(2400)
mhs2 = Industri(2000)

parent_mhs = ParentUniv(30)
parent_mhs.add(mhs1)
parent_mhs.add(mhs2)

parent_mhs.print_Universitas()
