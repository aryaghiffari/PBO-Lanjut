class king:
    def __init__(self, nama, level) -> None:
        self.nama = nama
        self.level = level
    def get_info (self):
        print(f"Nama : {self.nama}")
        print(f"Level : {self.level}")
class job:
    def __init__(self, Class, weapon) -> None:
        self.Class = Class
        self.weapon = weapon
    def get_info(self):
        print(f"Job : {self.Class}")
        print(f"Weapon : {self.weapon}")
class knight:
    def __init__(self,title, weapon) -> None:
        self.title = title
        self.weapon = weapon
    def get_info(self):
        print(f"Title : {self.title}")
        print(f"Weapon : {self.weapon}")
class Samurai (job,knight):
    def __init__(self, nama, level, Class, title, weapon) -> None:
        king.__init__(self, nama, level)
        job.__init__(self, Class,weapon)
        knight.__init__(self,title,weapon)
    def get_info(self):
        super().get_info()
        print(f"Nama : {self.nama}")
        print(f"Level : {self.level}")
        print(f"Job : {self.Class}")
        print(f"Weapon : {self.weapon}")
        print(f"Title : {self.title}")
info= Samurai("Argy Rem",300,"Samurai","Dragon Hunter","Katana")
info.get_info()