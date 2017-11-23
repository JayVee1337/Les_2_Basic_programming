# Oef 02: Bestudeer het bronbestand bieren.csv. (bron: http://www.belgourmet.be/nl/bieren/index.php).
# Door welke zaken wordt een bier gekenmerkt? Maak nu een dataklasse Bier.
#  Voorzie de klasse van de nodige attributen en properties.
# o In de setter wordt de nieuwe waarde gecontroleerd: een lege string wordt naar
# ‘onbekend’ omgezet.
# o Het alcoholpercentage moet tussen 0 en 100 liggen.
#  Programmeer de methode __init__()
#  Programmeer de methode __str__()
# Maak verschillende bieren aan. Wijzig nadien de attributen via de setter-methodes. Controleer
# of de functionaliteit in orde is.

#bieren gekenmerkt door: Nr;Naam;Brouwerij;Kleur;alcohol

class Bier:
    def __init__(self, nummer, naam, brouwerij, kleur, alcoholpercentage):
        self.nummer = nummer
        self.naam = naam
        self.brouwerij = brouwerij
        self.kleur = kleur
        self.alcoholpercentage = alcoholpercentage
    @property
    def nummer(self):
        return self.__nummer

    @nummer.setter
    def nummer(self, value):
        if value == '':
            self.__nummer = "onbekend"
        else: self.__nummer = value
    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        if value == '':
            self.__naam = 'onbekend'
        else: self.__naam = value

    @property
    def brouwerij(self):
        return self.__brouwerij

    @brouwerij.setter
    def brouwerij(self, value):
        if value == '0':
            self.__brouwerij = 'onbekend'
        else: self.__brouwerij = value

    @property
    def kleur(self):
        return self.__kleur

    @kleur.setter
    def kleur(self, value):
        if value =='0':
            self.__kleur = 'onbekend'
        else: self.__kleur = value

    @property
    def alcoholpercentage(self):
        return self.__alcoholpercentage

    @alcoholpercentage.setter
    def alcoholpercentage(self, value):
        if value == '':
            self.__alcoholpercentage = 'onbekend'
        elif value > 100 or value < 0:
            self.__alcoholpercentage = 'Impossibru'
        else:
            self.__alcoholpercentage = value

    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.nummer, self.naam, self.brouwerij, self.kleur, self.alcoholpercentage)



