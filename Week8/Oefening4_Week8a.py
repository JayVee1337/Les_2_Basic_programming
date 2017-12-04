#  Maak een applicatie waarmee men de kamerbezetting van een hotel kan beheren.
# Een receptionist zal je applicatie gebruiken om het kamerbeheer te doen.
# Maak hiervoor de volgende klassen:
#  Een klasse Hotelgast die de naam, voornaam en het adres moet bevatten.
#  Een klasse Verblijfsperiode die de startdatum en de einddatum (in tekstvorm) moet
# bevatten.
#  Een klasse Hotel met een dictionary kamerLijst waarbij voor elk kamernummer
# afzonderlijk bijgehouden wordt welke hotelgasten voor welke periode in de kamer
# aanwezig zijn. (Je kan hiervoor een dictionary({hotelgast:verblijfsperiode}) als value in
# de dictionary kamerLijst stoppen).
# Implementeer vervolgens methodes om:
#  Alle vrije kamers te printen
#  Alle bezette kamers te printen
#  Een reservatie te maken
#  Een reservatie op te zoeken a.d.h.v. de naam van een gast
#  De kamerbezetting te tonen
# Implementeer alle methodes.
# Test vervolgens alles voldoende uit.

class Verblijfsperiode:
    def __init__(self, startdatum, einddatum):
        self.startdatum = startdatum
        self.einddatum = einddatum

    @property
    def startdatum(self):
        return self.startdatum

    @startdatum.setter
    def startdatum(self, value):
        self.__startdatum = value

    @property
    def einddatum(self):
        return self.einddatum

    @einddatum.setter
    def einddatum(self, value):
        self.__einddatum = value

    def __str__(self): "De startdatum is {0}, de einddatum is {1}".format(self.startdatum, self.einddatum)