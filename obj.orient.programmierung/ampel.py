class Ampel(object):
    def __init__(self, anfangszustand):
        self.zustand = anfangszustand
        self.h = True

    def setzustand(self, z):
        self.zustand = z
        
    def schalten(self):
        if self.h == True:
            if self.zustand == 'rot':
                self.zustand = 'rotgelb'
            elif self.zustand == 'rotgelb':
                self.zustand = 'gruen'
            elif self.zustand == 'gruen':
                self.zustand = 'gelb'
            elif self.zustand == 'gelb':
                self.zustand = 'rot'
        else:
            return 'Nightmode'

    def getLampen(self):
        if self.h == True:
            if self.zustand == 'rot':
                lampen = (True, False, False)
            elif self.zustand == 'rotgelb':
                lampen = (True, True, False)
            elif self.zustand == 'gruen':
                lampen = (False, False, True)
            elif self.zustand == 'gelb':
                lampen = (False, True, False)
        else:
            lampen = (False, False, False, 'Nightmode')
        return lampen

    def hWechsel(self):
        if self.h == True:
            self.h = False
        else:
            self.h = True
