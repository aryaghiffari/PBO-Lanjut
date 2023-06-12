class Fahrenheit:
    def __init__(self, fahrenheit):
        self.f = fahrenheit

    def celcius (self):
        return (self.f-32)*5/9
    
    def kelvin(self):
        return (self.f+459.67)*5/9
    
    def reamur(self):
        return 4/9*(self.f-32)
    
fahrenheit = Fahrenheit(100)
print (f"Celcius: {fahrenheit.celcius()}")
fahrenheit = Fahrenheit(100)
print(f"Kelvin :{fahrenheit.kelvin()}")
fahrenheit = Fahrenheit(100)
print(f"Reamur: {fahrenheit.reamur()}")