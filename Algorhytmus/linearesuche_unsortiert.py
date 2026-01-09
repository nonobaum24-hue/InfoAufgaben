liste = [1,3,5,7,8,9,12,14,16,18,21,23,25,27,29,32,35,38,41,44,47,50,54,58,63]

d = int(input("Geben Sie eine Zahl ein: "))



def linearesuche_unsortiert(x, liste):
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
        if d == liste[Gl]:
            gefunden = True
            E = Gl
        else:
            if d < liste[Gl]:
                Gr = Gl - 1
            else: 
                Gl = Gl + 1
    return E

z = linearesuche_unsortiert(d, liste)
if z != -1:
    print("Die Zahl", d, "wurde an der Stelle", z, "gefunden.")
else:
    print("Die Zahl", d, "wurde nicht gefunden.")