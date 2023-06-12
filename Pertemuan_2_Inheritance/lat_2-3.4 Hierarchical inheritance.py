class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def get_name(self):
        self.name
        print(f"Nama : {self.name}")
    def get_color(self):
        self.color
        print(f"Warna : {self.color}")
class TwoDimensional(Shape):
    def __init__(self, name, color, sides):
        super().__init__(name, color)
        self.sides = sides
    def get_sides(self):
        self.sides
        print(f"Sisi : {self.sides}")
class ThreeDimensional(Shape):
    def __init__(self, name, color, faces):
        super().__init__(name, color)
        self.faces = faces
    def get_faces(self):
        self.faces
        print(f"Face : {self.faces}")
# Hierarchical Inheritance
class Sphere(ThreeDimensional):
    def __init__(self, name, color, faces, radius):
        super().__init__(name, color, faces)
        self.radius = radius
    def get_radius(self):
        self.radius
        print(f"Radius : {self.radius}")
a=Shape("Circle", "Blue")
a.get_name()
a.get_color()