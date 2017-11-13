# Oef02: Maak een applicatie die controleert of een bestand ‘test2.txt’ al dan niet bestaat.
# - Wanneer het bestand bestaat, dan wordt de functie ‘lees_bestand_in_met_lijnnummers’
# uit vorige oefening aangeroepen.
# - Wanneer het bestand nog niet bestaat, wordt de functie ‘schrijf_input_naar_bestand’
# aangeroepen.
# Deze functie maakt een nieuw bestand aan (met de bestandsnaam als parameter).
# Vervolgens vragen we meermaals aan de gebruiker om een lijn op te geven. Elke
# nieuwe lijn wordt onmiddellijk naar het bestand weggeschreven. De gebruiker kan
# afsluiten met het karakter “s” op een nieuwe lijn.
import os

def schrijf_input_naar_bestand(bestandsnaam):
    test2= open(bestandsnaam, 'w')
    lijn = input("geef een nieuwe lijn in, om af te sluiten voer je s in ")
    while lijn != 's':
        test2.write(lijn + '\n')
        lijn = input("geef een nieuwe lijn in, om af te sluiten voer je s in ")
    test2.close()

filename = "test2"


def lees_bestand_in_met_lijnnummers(bestandsnaam):
    test2 = open("test2", 'r')
    lijn = test2.readline().rstrip('\n')
    index=0
    while lijn != '':
        index = index+1
        print("{0}.{1}".format(index, lijn))
        lijn= test2.readline().rstrip('\n')
    test2.close()




if os.path.exists("test2") == True:
    lees_bestand_in_met_lijnnummers(filename)
else:
    schrijf_input_naar_bestand(filename)











