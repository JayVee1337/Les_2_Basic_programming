# Oef 01: Maak een klasse speler die naast een naam en voornaam ook een individuele score
# bijhoudt. Voorzie de klasse nu van:
#  de gevraagde properties met de nodige inputvalidatie
#  de klassieke methodes __init__() en __str__()
# Breid nu deze klasse uit zodat ook de totale score van het volledige team kan opgevraagd
# worden: dit is de som van alle individuele scores.
# (Let op: deze teamscore is voor elke speler gelijk).
# Voorzie een een static-methode om deze teamscore terug te geven.
# Test uit door verschillende objecten van deze klasse aan te maken.

class Spelers:
    #Static variable
    __teamscore = 0
    def __init__(self, naam,  voornaam, score):
        self.naam = naam
        self.voornaam = voornaam
        self.score = score
        Spelers.__teamscore += self.score
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
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if isinstance(value, int):
            self.__score = value
        else: self.__score = 0
    @staticmethod
    def getTeamScore():
        return Spelers.__teamscore#merk op: Speler ipv zelf

    def __del__(self):
        Spelers.__teamscore -= self.score

    def __str__(self):
        return "{0} {1} heeft een score van {2} en de teamscore is {3}".format(self.naam, self.voornaam, self.score, Spelers.__teamscore)