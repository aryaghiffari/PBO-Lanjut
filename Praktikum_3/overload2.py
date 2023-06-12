class hewan:
    def bersuara (self):
        return 'Kucing bersuara Meow'

class hewan2:
    def bersuara(self):
        return 'Anjing bersuara Guk Guk'
    
obj_hewan = hewan()
obj_hewan2 = hewan2()

for obj in [obj_hewan, obj_hewan2]:
    print(obj.bersuara())