# Oef 01: Maak een dataklasse Boek. Wat zijn de kenmerken waarmee een boek zich kan
# identificeren? Codeer nu deze dataklasse:
#  Voorzie de klasse van de nodige attributen en properties.
#  Programmeer de methode __init__()
#  Programmeer de methode __str__()
# Test uit door verschillende objecten van deze klasse aan te maken. Gebruik hiervoor een
# afzonderlijk bestand

class Boek:
    def __init__(self, titel, schrijver, aantal_paginas, hard_of_paperback, genre):
        self.titel = titel
        self.schrijver = schrijver
        self.aantal_paginas = aantal_paginas
        self.hard_of_paperback = hard_of_paperback
        self.genre = genre
    def __str__(self):
        return ("{0}, geschreven door {1}, is een {4}, heeft {2} pagina's en wordt het meest verkocht als {3}".format(self.titel, self.schrijver, self.aantal_paginas, self.hard_of_paperback, self.genre))