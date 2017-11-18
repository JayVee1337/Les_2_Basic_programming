# Oef04: Gegeven het bronbestand ‘spelers.txt’. Kopieer dit bronbestand in een submap
# ‘tekstbestanden’ in uw projectmap. Analyseer het bronbestand: elke regel bestaat uit de
# gegevens van een voetbalspeler. Maak een applicatie die het bronbestand inleest, en
# vervolgens 11 verschillende spelers willekeurig selecteert om als ploegopstelling te kunnen
# fungeren. Deze 11 spelers worden in een nieuw bestand weggeschreven.
# Bepaal vooraf welke datastructuur je zal gebruiken om alle data bij te houden.
# Werk vervolgens in deelproblemen door o.a. gebruik te maken van onderstaande functies:
# - Functie ‘inlezen_spelers’ die het bronbestand correct inleest en data in een
# datastructuur bijhoudt
# - Functie die in staat is om alle spelers uit de gekozen datastructuur af te printen
# - Functie ‘selecteer_random_elftal’ die in staat is om 11 verschillende spelers te
# selecteren
# - Functie ‘opslaan_ploegopstelling’ die in staat is om een opstelling naar een tekstbestand
# weg te schrijven.
# Test voldoende uit.
import random
import os

def inlezen_spelers(bestandsnaam):
    if os.path.exists(bestandsnaam):
        bestand = open(bestandsnaam, 'r')
        spelers= []
        lijn = bestand.readline()
        while(lijn):
            spelers.append(lijn.rstrip('\n'))
            lijn = bestand.readline()


        bestand.close()
        return spelers
    else: print ("file bestaat niet")

def selecteer_random_elftal(spelerslijst):
    gekozen_ploeg = []
    krimpende_lijst = spelerslijst

    for aantal in range(0,11):
        willekeurig_getal = random.randrange(0, len(krimpende_lijst))
        gekozen_ploeg.append(krimpende_lijst[willekeurig_getal])
        krimpende_lijst.pop(willekeurig_getal)
    print(gekozen_ploeg)

def opslaan_ploegopstelling(spelerslijst):
    gekozen_ploeg = []
    krimpende_lijst = spelerslijst

    for aantal in range(0,11):
        willekeurig_getal = random.randrange(0, len(krimpende_lijst))
        gekozen_ploeg.append(krimpende_lijst[willekeurig_getal])
        krimpende_lijst.pop(willekeurig_getal)
    print(gekozen_ploeg)
    ploeg = open("ploegopstelling.txt", 'r')
    ploeg.write(gekozen_ploeg)
spelers =inlezen_spelers("Tekstbestand/Spelers.txt")
selecteer_random_elftal(spelers)
opslaan_ploegopstelling(spelers)