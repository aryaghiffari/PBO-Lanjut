class King:
    def __init__(self,nama,level) -> None:
        self.nama = nama
        self.level = level
    def attack (self):
        print (self.nama, "Sword up")
class Knight (King):
    def __init__(self, nama, level, weapon) -> None:
        super().__init__(nama, level)
        self.weapon = weapon
    def sword_skills (self):
        print ("Realise of Power")
KnightA = Knight ("Argy Rem", 300, "Night Sky Blade")
KnightA.sword_skills()
KnightA.attack()