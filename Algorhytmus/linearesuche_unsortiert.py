liste = [42, 7, 89, 13, 56, 2, 98, 31, 64, 17]

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

print(linearesuche_unsortiert(56, liste))