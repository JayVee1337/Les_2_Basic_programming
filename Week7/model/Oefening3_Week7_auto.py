# Oef 03: Maak een dataklasse Auto waarbij volgende zaken worden bijgehouden: kleur, merk,
# brandstof, model, km-stand.
# Hoe kan je er voor zorgen dat enkel de attributen kmstand en kleur nadien gewijzigd kunnen
# worden?
# Voeg ook een methode ‘rijden’ met de parameter extra_km toe: hiermee wordt de km-stand
# van de auto verhoogd.
# Test alles uit: maak een list aan met verschillende voertuigen. Laat vervolgens elk voertuig uit
# de list een random afstand afleggen. Print nadien van elk voertuig de km-stand af.


# __ maakt private!!
class Auto:
    def __init__(self, kleur, merk, brandstof, model, kmstand = 0):

        self.kleur = kleur
        self.__merk = merk
        self.__brandstof =brandstof
        self.__model = model
        self.kmstand = kmstand
    @property
    def merk(self):
        return self.__merk
    @property
    def brandstof(self):
        return self.__brandstof
    @property
    def model(self):
        return self.__model
    @property
    def kleur(self):
        return self.__kleur #waarom __kleur?? zonder __ krijg je een infinite loop!!!

    @kleur.setter
    def kleur(self, value):
        self.__kleur = value
    @property
    def kmstand(self):
        return self.__kmstand

    @kmstand.setter
    def kmstand(self, value):
        if value > 0:
            self.__kmstand = value
        else: self.__kmstand = 0

    def rijden(self, aantal_km):
        self.kmstand += aantal_km

    def __str__(self):
        return '{0} {1} kmstand: {2}'.format(self.__merk, self.__model, self.kmstand)
