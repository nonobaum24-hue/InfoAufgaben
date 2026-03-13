#parent
class Ampel(object):
    def __init__(self, pListeZustaende):
        self.listeZustaende = pListeZustaende
        self.indexAktuellerZustand = 0

    def schalten(self):
        if self.indexAktuellerZustand < len(self.listeZustaende)-1:
            self.indexAktuellerZustand = self.indexAktuellerZustand + 1
        else:
            self.indexAktuellerZustand = 0

    def getZustand(self):
        return self.listeZustaende[self.indexAktuellerZustand]

    def setZustand(self, z):
        self.indexAktuellerZustand = self.listeZustaende.index(z)

#Auto
class AmpelAuto(Ampel):
    def __init__(self, anfangszustand):
        self.listeZustaende = ['rot', 'rotgelb', 'gruen', 'gelb']
        self.indexAktuellerZustand = self.listeZustaende.index(anfangszustand)

    def getLampen(self):
        zustand = self.listeZustaende[self.indexAktuellerZustand]
        if zustand == 'rot':
            lampen = (True, False, False)
        elif zustand == 'rotgelb':
            lampen = (True, True, False)
        elif zustand == 'gruen':
            lampen = (False, False, True)
        elif zustand == 'gelb':
            lampen = (False, True, False)
        return lampen

#Fußgänger
class AmpelFuß(Ampel):
    def __init__(self, anfangszustand):
        self.listeZustaende = ['rot', 'gruen']
        self.indexAktuellerZustand = self.listeZustaende.index(anfangszustand)

    def getLampen(self):
        zustand = self.listeZustaende[self.indexAktuellerZustand]
        if zustand == 'rot':
            lampen = (True, False)
        elif zustand == 'gruen':
            lampen = (False, True)
        return lampen

#amerika
class AmpelAmi(Ampel):
    def __init__(self, anfangszustand):
        self.listeZustaende = ['rot', 'gruen', 'gelb', 'stop']
        self.indexAktuellerZustand = self.listeZustaende.index(anfangszustand)

    def getLampen(self):
        zustand = self.listeZustaende[self.indexAktuellerZustand]
        if zustand == 'rot':
            lampen = (True, False, False, False)
        elif zustand == 'stop':
            lampen = (False, False, False, True)
        elif zustand == 'gruen':
            lampen = (False, False, True, False)
        elif zustand == 'gelb':
            lampen = (False, True, False, False)
        return lampen

    def schalten(self):
        if self.indexAktuellerZustand < len(self.listeZustaende)-2:
            self.indexAktuellerZustand = self.indexAktuellerZustand + 1
        else:
            self.indexAktuellerZustand = 0

    def off(self):
        self.indexAktuellerZustand = 3

#Fuß
a=AmpelAmi('rot')
a.schalten()
print(a.getZustand())

a.off()
print(a.getZustand())
