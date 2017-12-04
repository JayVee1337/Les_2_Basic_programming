# Oef 2: Zoek de klasse Bier uit labo week 7 op. Pas deze klasse nu aan zodat
# - in elke resp. setter-property een controle gebeurt op de nieuwe doorgegeven waarde
# o biernaam, brouwerijnaam, kleur: nieuwe waarde is een string en mag niet leeg zijn
# o alcoholpercentage: nieuwe waarde is een float en ligt tussen 0 en 100
# - indien de nieuwe waarde niet voldoet wordt een ValueError teruggegeven
# Test uit door:
# - maak een correct bier aan. Wijzig nadien de naam van het bier in een lege string.
# - maak een bier aan waarbij je voor de brouwerij een lege string doorgeeft.
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
        if isinstance(value, str) and value != '':
            self.__naam = value
        else:
            raise ValueError('Biernaam is geen string!')


    @property
    def brouwerij(self):
        return self.__brouwerij

    @brouwerij.setter
    def brouwerij(self, value):
        if isinstance(value, str) and value != None:
            self.__brouwerij = value
        else: raise ValueError('Brouwerij is geen string!!!')

    @property
    def kleur(self):
        return self.__kleur

    @kleur.setter
    def kleur(self, value):
        if isinstance(value, str)and value !='0':
            self.__kleur = value

        else: raise ValueError

    @property
    def alcoholpercentage(self):
        return self.__alcoholpercentage

    @alcoholpercentage.setter
    def alcoholpercentage(self, value):
        if isinstance(value, float) and value in range (0, 101):
            self.__alcoholpercentage = value
        else:
            raise ValueError ('Alcoholpercentage ligt niet tussen 0 en 100 (en is mogelijks geen float)')


    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.nummer, self.naam, self.brouwerij, self.kleur, self.alcoholpercentage)
