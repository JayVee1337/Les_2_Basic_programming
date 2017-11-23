#klasse die een student beschrijft
#naam van de klasse ALTIJD met hoofdletter
#geen hoofdletter => +- 3 minpunten
class Student:
    # __ betekent methode die door python wordt aangeroepen
    #wordt uitgevoerd bij het aanmaken of instantiëren van het object
    def __init__(self,naam, voornaam, geslacht, leeftijd):
        #Hier werken we met de properties
        #dus hier geen self.__naam (= private variable)
        self.naam = naam
        self.voornaam = voornaam
        self.leeftijd = leeftijd
        self.geslacht = geslacht
    @property
    def naam(self):
        return self.__naam
    
    @naam.setter
    def naam(self, value):
        if len(value)>=2:
            self.__naam = value
        else:
            print("kies een langere naam")
    @property
    def voornaam(self):
        return self.__voornaam


    @voornaam.setter
    def voornaam(self, value):
        if len(value) > 1:
            self.__voornaam = value
        else: print("unknown")


    #wordt automatisch aangeroepen door python als we het object willen voorstellen of printen
    #naam van de klasse + referentieverwijzing naar geheugen
    #wij kunnen die methode, definitie gaan overschrijven of overriden
    def __str__(self):
        return "{0} {1}".format(self.naam, self.voornaam)

