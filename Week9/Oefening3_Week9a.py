from Week9.Oefening3_Week9 import Bier


def verwerk_bierenfile(bestandsnaam):
    return Bier.inlezen_bieren(bestandsnaam)


bierenlijst = verwerk_bierenfile('bieren.csv')
for item in bierenlijst:
    print(item)