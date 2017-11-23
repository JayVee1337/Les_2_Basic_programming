# Oef 05: Maak een dataklasse Winkelkar dat als private attribuut een list van producten (String)
# bijhoudt. Voorzie de klasse van volgende methodes:
#  Programmeer de methode __init__()
#  Programmeer de methode __str__()
#  ‘Read-only’ property-methode ‘producten’ dat de lijst terug geeft.
#  Methode ‘voeg_product_toe(nieuw_product)’ dat een nieuw product aan het winkelkarretje
# toevoegt.
#  Methode ‘verwijder_product(product)’ dat een product uit het winkelkarretje verwijdert.
#  Zorg ervoor dat de +-operator toegepast kan worden:
# o zodat twee winkelkarretjes bij elkaar kunnen opgeteld worden en een nieuw
# winkelkarretje opleveren (welke methode moet hiervoor toegevoegd worden?)
# o zodat het bestaande winkelkarretje uitgebreid wordt met de producten uit een
# andere winkelkarretje (welke methode moet hiervoor toegevoegd worden?)
# Test alles uit:
#  Maak 2 winkelkarrtjes aan. Voeg verschillende producten aan elk toe.
# Print nadien beide af.
#  Tel beide winkelkarrtejes op via de plus-operator. Print resultaat af.

class Winkelkar:
    def __init__(self):
        self.__producten = []

    @property
    def producten(self):
        return self.__producten

    def voeg_product_toe(self, product):
        self.producten.append(product)

    def verwijder_product(self, product):
        self.producten.remove(product)

    def __iadd__(self, other):
        w= Winkelkar()
        w.__producten = self.producten + other.producten
        return w

    def __add__(self, other): #methode wordt aangeroepen door + operator
        w = Winkelkar()
        w.__producten = self.producten + other.producten
        return w

    def __str__(self):
        lijst = "Producten in kar : "
        for product in self.producten:
            lijst+=product + ", "
        return lijst