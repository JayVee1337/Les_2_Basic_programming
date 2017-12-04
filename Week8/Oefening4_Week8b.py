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
import random
class Hotel:
    __aantal_hotels = 0
    def __init__(self, aantal_Kamers):
        self.__kamerLijst = {} #kamerlijst niet boven init omdat niet elk hotel uit een keten hetzelfde aantal kamers heeft!
        if aantal_Kamers > 0 :
            for teller in range(1, aantal_Kamers + 1):
                dict_verblijf_in_kamer = {}
                self.__kamerLijst.update({teller: dict_verblijf_in_kamer})
        Hotel.__aantal_hotels +=1

    @property
    def lege_kamers(self):
        vrije_kamers = []
        for key, value in self.__kamerLijst.items():
            if len(value) == 0:
                vrije_kamers.append(key)

        return vrije_kamers

    def wijs_kamer_random_toe(self, hotelgast, verblijfsperiode):

        #zoek een random vrije kamer
        kamernummer = random.randrange(0, len())
        #vervangen door een random vrije kamer
        #controle of eer nog een kamer vrij is (anders: alle kamers zijn bezet
        dict_verblijf_in_kamer = self.__kamerLijst[3]
        #gast en verblijfsperiode toevoegen aan dict_verblijf_in_kamer
        dict_verblijf_in_kamer [hotelgast] = verblijfsperiode
        return kamernummer

