# Oef02: Maak één functie ‘print_tuple’ die de verschillende elementen overloopt waarbij elk element
# samen met zijn index wordt afgeprint.
# De functie heeft als parameters een naam (voor de tuple) en de tuple zelf.
# Voorbeeld:

def print_tuple(tuple, naam):
    print("de elementen van de tuple {0} zijn".format(naam))
    for item in tuple:
        print ("{0} : {1}".format(tuple.index(item), item))

nmct= ("1NMCT", "2NMCT", "3NMCT")
devine = ("1Devine", "2Devine", "3Devine")
print_tuple(nmct, "NMCT")
print_tuple(devine, "Devine")