from kartenstapel import *

h1 = Kartenhaufen()
h2 = Kartenhaufen()
k = Kartenstapel()

print(k.kartenListe)
print()
k.mischen()
print('karten gemnischt')
print()
print('---------------------------------------------------')
print('Spiel Beginnt')
print('---------------------------------------------------')
print()

for i in range(2):
    neueKarte = k.karteZiehen()
    h1.hinzufuegen(neueKarte)
    neueKarte2 = k.karteZiehen()
    h2.hinzufuegen(neueKarte2)
    print('Spieler 1: ', neueKarte, ' --- Spieler 2: ', neueKarte2)
    print()

print('Spieler 1 Wert: ', h1.wert, ' --- Spieler 2 Wert: ', h2.wert)

spielzuende = False
while spielzuende == False:
    i1 = input('Spieler 1: Möchtest du eine weitere Karte ziehen? (j/n) ')
    if i1 == 'j':
        neueKarte = k.karteZiehen()
        h1.hinzufuegen(neueKarte)
        print('Spieler 1: ', neueKarte)
        print('Spieler 1 Wert: ', h1.wert)
    elif i1 == 'n':
        spielzuende = True
    i2 = input('Spieler 2: Möchtest du eine weitere Karte ziehen? (j/n) ')
    if i2 == 'j':
        neueKarte2 = k.karteZiehen()
        h2.hinzufuegen(neueKarte2)
        print('Spieler 2: ', neueKarte2)
        print('Spieler 2 Wert: ', h2.wert)
    elif i2 == 'n':
        spielzuende = True
    if h1.wert > 21 or h2.wert > 21:
        spielzuende = True

print()
print('---------------------------------------------------')
print('Spiel Ende')
print('---------------------------------------------------')
print('Spieler 1 Wert: ', h1.wert, ' --- Spieler 2 Wert: ', h2.wert)
if h1.wert > 21 and h2.wert > 21:
    print('Beide Spieler haben verloren')
elif h1.wert > 21:
    print('Spieler 1 hat verloren, Spieler 2 gewinnt')
elif h2.wert > 21:
    print('Spieler 2 hat verloren, Spieler 1 gewinnt')
elif h1.wert > h2.wert:
    print('Spieler 1 gewinnt')
elif h2.wert > h1.wert:
    print('Spieler 2 gewinnt')