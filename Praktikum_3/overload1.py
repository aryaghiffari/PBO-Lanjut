class suara_hewan:
    def hallo (self, suara= None):
        if suara is not None:
            print('Kucing'+suara)
        else:
            print ('Bersuara')
sound = suara_hewan()
sound.hallo()
sound.hallo('Meow')