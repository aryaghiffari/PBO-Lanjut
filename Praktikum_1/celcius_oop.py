# Nama  : Arya Ghiffari
# Nim   : 210511004
# Kelas : D

class Celcius:
    def __init__(self, celcius):
        self.c = celcius

    def fahrenheit(self):
        return (self.c * 9/5) + 32
    
    def kelvin(self):
        return self.c + 273.15
    
    def reamur(self):
        return self.c * 4/5
    
celciusA = Celcius(75)
print(f"Fahrenheit: {celciusA.fahrenheit()}")
celciusA = Celcius(60)
print(f"Kelvin: {celciusA.kelvin()}")
celciusA = Celcius(90)
print(f"Reamur: {celciusA.reamur()}")