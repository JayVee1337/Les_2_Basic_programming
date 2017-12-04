# Oef 02: Maak een dataklasse Geboortedatum.
# Zorg ervoor dat dag, maand en jaartal bijgehouden worden.
# Voorzie nu zelf de klasse van:
#  De gevraagde properties.
# Bouw controles in wanneer dag/maand/jaartal gewijzigd worden.
#  Programmeer de methode __init__()
#  Programmeer de methode __str__()
# Breid de klasse nu vervolgens uit:
#  Hou het aantal gecreërde objecten van de klasse Geboortedatum bij.
#  Maak een static methode om deze property op te vragen.
#  Maak een static methode die een willekeurige geboortedatum genereert
#  Maak een static methode die een list van willekeurige geboortedatums genereert en
# teruggeeft. De parameter is het gewenste aantal.
#  Integreer een methode die instaat om de gelijkheid tussen twee geboortedatums te
# controleren. Bepaal eerst vooraf wanneer twee geboortedatums aan elkaar gelijk zijn.
# (Tip: gebruik operator overloading!)
#  Maak een (gewone) methode met als parameter een object Geboortedatum, die
# controleert of beide op dezelfde dag verjaren (m.a.w. dag & maand zijn gelijk)
# Test uit door verschillende objecten van deze klasse aan te maken.
# Plaats deze test in een ander afzonderlijk python-bestand.
import datetime
from itertools import count

class Geboortedatum:
    def __init__(self,dag, maand, jaartal):
        self.maand = maand
        self.dag = dag
        self.jaartal = jaartal
    @property
    def jaartal(self):
        return self.jaartal

    @jaartal.setter
    def jaartal(self, value):
        if self.jaartal in range (1900,2017):
            self.__jaartal = value
        else: self.jaartal = '?'

    @property
    def maand(self):
        return self.__maand

    @maand.setter
    def maand(self, value):
        if self.maand in range (1,13):
            self.__maand = value
        else:
            self.__maand = '?'
    def controleer_dag(self, nieuwe_dag):
        if self.maand in [1, 3, 5, 7, 8, 10, 12]:
            if nieuwe_dag in range(1, 32):
                return True
        if self.maand == 2:
            if nieuwe_dag in range(2, 30):
                return True
        else:
            if nieuwe_dag in range(1, 31):
                return True
            return False

    @property
    def dag(self):
        return self.dag

    @dag.setter
    def dag(self, value):
        if self.controleer_dag(value):
            self.dag = value
        else:
            self.dag = None



    def __str__(self):
        return "De geboortedatum is {0}/{1}/{2}".format(self.dag, self.maand, self.jaartal)