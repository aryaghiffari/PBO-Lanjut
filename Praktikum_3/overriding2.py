class hewan:
    def bersuara(self):
        print('Meong')

class hewan2(hewan):
    def bersuara(self,perilaku = 'Dengan Lantang'):
        super().bersuara()
        print(f"seekor Kucing bersuara  Meong {perilaku}")

a = hewan()
b = hewan2()
a.bersuara()
b.bersuara()  