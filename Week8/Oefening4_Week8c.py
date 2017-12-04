# Maak een applicatie waarmee men de kamerbezetting van een hotel kan beheren.
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


from Week8.Oefening4_Week8b import Hotel
from Week8.Oefening4_Week8a import Verblijfsperiode
from Week8.Oefening4_Week8 import Hotelgast


gh = Hotel(5)

opdracht = input("Geef een opdracht: \n \t 'k' om vrije kamers te zien \n \t 'r' om een reservatie te maken \n \t 'z' om een reservatie te zoeken \n \t 'b' om een kamerbezetting te zien \n \t 's' om te stoppen \n Opdracht = ")
while opdracht != 's':

    None






print(opdracht)
print (gh.lege_kamers)


#hoe maken we een reservering???