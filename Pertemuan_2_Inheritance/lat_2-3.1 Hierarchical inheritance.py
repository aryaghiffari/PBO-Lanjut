class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def get_name(self):
        self.name
        print(f"Nama :{self.name}")
    def get_color(self):
        self.color
        print(f"Warna :{self.color}")
class Mammal(Animal):
    def __init__(self, name, color, fur):
        super().__init__(name, color)
        self.fur = fur
    def get_fur(self):
        self.fur
        print(f"Bulu : {self.fur}")
class Bird(Animal):
    def __init__(self, name, color, wingspan):
        super().__init__(name, color)
        self.wingspan = wingspan
    def get_wingspan(self):
        self.wingspan
        print(f"Bentang sayap : {self.wingspan}")
# Hierarchical Inheritance
class Reptile(Mammal):
    def __init__(self, name, color, fur, scale):
        super().__init__(name, color, fur)
        self.scale = scale
    def get_scale(self):
        self.scale
        print(f"Perilaku : {self.scale}")
        
object = Reptile("Kucing","Pink","Lembut","imut")
object.get_name()
object.get_color()
object.get_scale()
object.get_fur()