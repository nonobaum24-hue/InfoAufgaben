# Rucksackproblem
from random import *

gegenstaende = [(3.5, 375), (2.5, 300), (2.0, 100), (3.0, 225), (1.0, 50),
               (1.75, 125), (0.75, 75), (3.0, 275), (2.5, 150), (2.25, 50)]
grenzgewichtRucksack = 15.0



# Funktionen zur Erzeugung einer Lösung

def gesamtGewicht(kombination):
    gesamtGewicht = 0
    for stelle, i in enumerate(kombination):
        if i == '1':
            gewicht = gegenstaende[stelle][0]
            gesamtGewicht += gewicht
    return gesamtGewicht

def gesamtWert(kombination):
    gesamtWert = 0
    for stelle, i in enumerate(kombination):
        if i == '1':
            wert = gegenstaende[stelle][1]
            gesamtWert += wert
    return gesamtWert

def erzeugeKombinationAusZahl(zahl):
    kombination = bin(zahl)[2:]
    while len(kombination) < len(gegenstaende):
        kombination = '0' + kombination
    return str(kombination)

def alleKombinationen():
    anzahlKombinationen = 2**len(gegenstaende)
    zahl = 0
    while zahl < anzahlKombinationen:
        kombination = erzeugeKombinationAusZahl(zahl)
        print(kombination, gesamtWert(kombination), gesamtGewicht(kombination))
        zahl = zahl + 1

def optimaleLoesung(gegenstaende):
    kombination = '0' * len(gegenstaende)
    maxKombination = kombination
    maxWert = gesamtWert(kombination)
    anzahlKombinationen = 2**len(gegenstaende)
    zahl = 0
    while zahl < anzahlKombinationen:
        kombination = erzeugeKombinationAusZahl(zahl)
        if gesamtWert(kombination) > maxWert and gesamtGewicht(kombination) <= grenzgewichtRucksack:
            maxKombination = kombination
            maxWert = gesamtWert(kombination)
        zahl = zahl + 1
    return (maxKombination, maxWert, gesamtGewicht(maxKombination))

print(optimaleLoesung(gegenstaende))
