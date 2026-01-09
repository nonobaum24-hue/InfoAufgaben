liste = [
('Krause','Stefanie','Brandenburgische Str. 20','74343,Sachsenheim'),
('Brandt','Mandy','Scharnweberstrasse 84','68199','Mannheim Almenhof'),
('Möller','Jens','Schoenebergerstrasse 47','08313,Bernsbach'),
...
]

d = int(input("Geben Sie eine Zahl ein: "))



def linearesuche(x, liste):
    i = 0
    E = -1
    gefunden = False
    while i < len(liste) and gefunden == False:
        if liste[i] == x:
            gefunden = True
            E = i
        else:
            i = i+1
    return E

def binsuche_sortiert(d, liste):
    E = -1
    Gl = d
    Gl = 0
    Gr = len(liste) - 1
    gefunden = False
    while gefunden == False and Gr >= Gl:
        m = (Gl + Gr) // 2
        if liste[m] == d:
            gefunden = True
            E = m
        elif d < liste[m]:
            Gr = m -1
        elif d > liste[m]:
            Gl = m + 1
    return E

from listenoperationen_zum_laden_und_speichern import *

def suchen(name, liste):
    indexErgebnis = -1
    gefunden = False
    links = 0
    rechts = len(liste)-1
    while not gefunden and links <= rechts:
        mitte = (links + rechts) // 2
        if name == liste[mitte][0]:
            gefunden = True
            indexErgebnis = mitte
        elif name < liste[mitte][0]:
            rechts = mitte-1
        else:
            links = mitte+1
    return indexErgebnis

# Test
text = textAusDatei('adressdaten_sortiert_name.csv')
listeDaten = tupelListeAusText(text)
index = suchen('Schmitt', listeDaten)
print(index)