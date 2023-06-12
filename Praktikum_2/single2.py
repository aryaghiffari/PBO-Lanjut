class semesta:
    def __init__(self, planet, urutan) -> None:
        self.planet= planet
        self.urutan= urutan
    def bergerak (self):
        print (self.planet, "Mengelilingi matahari")
class bumi (semesta):
    def __init__(self, planet, urutan,satelit ) -> None:
        super().__init__(planet, urutan)
        self.satelit = satelit
    def life (self):
        print ("Bumi dapat dihuni")
BumiA = bumi ("Bumi", 3, "bulan")
BumiA.bergerak()
BumiA.life()