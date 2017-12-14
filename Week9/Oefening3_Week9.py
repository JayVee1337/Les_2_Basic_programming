# Oef 3: download het bronbestand ‘bieren.csv’. Breid de klasse Bier uit (test elke methode afzonderlijk
# uit!):
# - met een static methode ‘inlezen_bieren’ die in staat is om het bronbestand in te lezen en een
# list van bieren terug te geven. Opgelet: niet elke lijn uit het bestand is correct opgebouwd!
# Sommige lijnen bevatten te weinig onderdelen waardoor geen object van de klasse Bier
# correct kan gevormd worden. Deze lijnen mogen overgeslagen worden. Pas hiervoor
# exception handling toe.
# - met een static methode ‘zoek_bieren_op_naam’ met parameters een list van objecten van de
# klasse Bier én een gezochte naam. Doorloop alle bieren en geef enkel deze bieren terug
# waarvan de gezochte naam geheel of gedeeltelijk in de biernaam voorkomt.
# - met een static methode ‘zoek_bieren_op_alcoholpercentage’ met parameters een list van
# objecten van de klasse Bier, een minimum alcohol percentage én een maximum alcohol
# percentage. Doorloop alle bieren en geef enkel deze bieren terug waarvan het
# alcoholpercentage tussen de doorgegeven grenzen valt.
# - met een static methode ‘zoek_bier_uit_brouwerij’ met parameters een list van objecten van de
# klasse Bier én een brouwerijnaam. Doorloop alle bieren en geef enkel deze bieren terug
# afkomstig uit de doorgegeven brouwerij.
# - zodat een list van bier-objecten op basis van het alcoholpercentage van klein naar groot kan
# gesorteerd worden.
# Test alle nieuwe methodes voldoende uit.
# Maak tenslotte een testprogramma waarmee je als gebruiker het bovenstaande kan uittesten. Een
# voorbeeldoutput vind je hieronder:
import csv
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
        if isinstance(value, float) == '':
            self.__alcoholpercentage = 'onbekend'
        elif value > 100 or value < 0:
            self.__alcoholpercentage = 'Impossibru'
        else:

            self.__alcoholpercentage = (value)


    @staticmethod
    def inlezen_bieren(bestandsnaam):

        bieren = []
        fo = open(bestandsnaam, 'r')
        lijn = fo.readline()  # eerste lijn (titel) mag weg
        lijn = fo.readline()
        while lijn != "":
            try:
                delen = lijn.split(';')  # ik krijg list met data van de verschillende kolommen
                delen[4].rstrip('\n')
                bier = Bier(int(delen[0]), delen[1], delen[2], delen[3], float(delen[4]))
                (delen[4].replace(',','.'))

                bieren.append(bier)
            except ValueError as ex:
                print(ex)
            lijn = fo.readline()
        fo.close()
        return bieren
    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.nummer, self.naam, self.brouwerij, self.kleur, self.alcoholpercentage)


