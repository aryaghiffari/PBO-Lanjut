# Nama  : Arya Ghiffari
# Nim   : 210511004
# Kelas : D

class Celcius:
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def to_kelvin(celsius):
        return celsius + 273.15
    
    @staticmethod
    def to_reamur(celsius):
        return celsius * 4/5
    
mycelcius = 70
myfahrenheit = Celcius.to_fahrenheit(mycelcius)
print("konversi ",mycelcius, "derajat celcius adalah ",myfahrenheit, "derajat fahrenheit")
mykelvin = Celcius.to_kelvin(mycelcius)
mycelcius = 60
print ("konversi ",mycelcius, "derajat celcius adalah ",mykelvin, "derajat Kelvin")
mycelcius = 90
myreamur = Celcius.to_kelvin(mycelcius)
print ("konversi ",mycelcius, "derajat celcius adalah ",myreamur, "derajat Reamur")