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

class Hotelgast:
    def __init__(self, naam, voornaam, adres):
        self.naam = naam
        self.voornaam = voornaam
        self.adres = adres

    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        self.__naam = value

    @property
    def voornaam(self):
        return self.__voornaam

    @voornaam.setter
    def voornaam(self, value):
        self.__voornaam = value

    @property
    def adres(self):
        return self.__adres

    @adres.setter
    def adres(self, value):
        self.__adres = value

    def __str__(self): "De nieuwe hotelgast is {} {}, adres {}".format(self.naam, self.voornaam, self.adres)
