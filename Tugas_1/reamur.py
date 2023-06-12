class Reamur:
    def __init__ (self,reamur):
        self.r = reamur
    
    def celcius (self):
        return 5/4*self.r
    
    def farenheit (self):
        return (9/4*self.r)+32
    
    def kelfin (self):
        return 5/4*self.r+273
    
reamur = Reamur(100)
print(f"Celcius :{reamur.celcius()}")
reamur = Reamur(100)
print(f"Farenheit :{reamur.farenheit()}")
reamur = Reamur(100)
print(f"Kelvin :{reamur.kelfin()}")