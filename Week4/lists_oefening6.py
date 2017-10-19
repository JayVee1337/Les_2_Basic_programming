#  Maak een functie ‘kies_element’ aan met als parameter een list. De functie kiest een
# willekeurig element uit de doorgegeven list en geeft deze terug. Test deze functie met
#  een list met strings, nl. de verschillende maanden
#  een list met getallen
# Print telkens het gekozen element af.

import random

maanden = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"]
Getallen = list(range(1,201))

def kies_element_maand(lijst):
    Gekozen_Maand =    random.choice(maanden)
    print("De gekozen maand is {0}".format(Gekozen_Maand))

def kies_element_getal(lijst):
    Gekozen_Getal= random.choice(Getallen)
    print("{0} is het gekozen getal".format(Gekozen_Getal))

kies_element_maand(maanden)
kies_element_getal(Getallen)