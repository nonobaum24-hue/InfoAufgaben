from kartenstapel import *

h1 = Kartenhaufen()
h2 = Kartenhaufen()
k = Kartenstapel()

print(k.kartenListe)
print()
k.mischen()
print(k.kartenListe)
print()
print('---------------------------------------------------')
print('Spiel Beginnt')
print('---------------------------------------------------')

for i in range(2):
    neueKarte = k.karteZiehen()
    h1.hinzufuegen(neueKarte)
    neueKarte2 = k.karteZiehen()
    h2.hinzufuegen(neueKarte2)
    print('Spieler 1: ', neueKarte, ' --- Spieler 2: ', neueKarte2)
    print()

print('Spieler 1 Wert: ', h1.wert, ' --- Spieler 2 Wert: ', h2.wert)
