class Kelvin:
    def __init__(self, kelvin):
        self.k = kelvin
    
    def celcius (self):
        return self.k - 273
    
    def farenheit (self):
        return 9/5*(self.k-273)+32
    
    def reamur (self):
        return 4/5*(self.k-273)
    
kelvin = Kelvin(335)
print (f"Celcius : {kelvin.celcius()}")
kelvin = Kelvin(335)
print (f"Farenheit : {kelvin.farenheit()}")
kelvin = Kelvin(335)
print (f"Reamur : {kelvin.reamur()}")