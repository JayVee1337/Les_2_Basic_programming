# Oef05: Gegeven het bronbestand ‘MorseVertaling.txt’.
# Kopieer dit bronbestand in een submap ‘tekstbestanden’ in uw projectmap.
# Analyseer het bronbestand: het bestaat uit een opsomming van letters met bijhorende
# morsevertaling. Merk op dat de eerste lijn van het bestand hier niet bijhoort.
# Maak een applicatie die bestaat uit:
# - Dictionary ‘morse_dictionary’
# - Functie ‘inlezen_morse_bestand’:
# Het morse-bestand correct inlezen en de data in de dictionary bijhoudt (waarom?)
# - Functie die in staat is om de dictionary morse_dictionary af te printen.
# - Functie ‘vertaal_tekst_in_morse’ met als parameter een string (te_vertalen_tekst) die
# de doorgegeven tekst vertaalt en nadien de vertaling teruggeeft.
# Deze functie maakt gebruik van volgende functie.
# - Functie ‘vertaal_letter’ met als parameter een letter (string). Deze functie controleert
# of de letter in de dictionary aanwezig is.
# Indien zo wordt de vertaling teruggegeven, indien niet zo wordt een ‘?’ terug gegeven.

morse_dictionary = {}
morse = open("Tekstbestand/MorseVertaling.txt")

def inlezen_morse_bestand(bestand):

    for line in morse:
        (key,val) = line.strip().split(";", 43)
        morse_dictionary [key.strip()] = val.strip()
    morse_dictionary.pop("letter")
def print_morse(bestand):
    inlezen_morse_bestand(morse)
    print(morse_dictionary)
def vertaal_letter(letter):
    inlezen_morse_bestand(morse)
    if letter in morse_dictionary:
        print(morse_dictionary[letter])
    else:print("??")
def vertaal_tekst_in_morse(woord):
    woord = input("geef een tekst op die naar morse vertaald moet worden, gebruik geen hoofletters!!: ")
    inlezen_morse_bestand(morse)
    letters = list(woord)
    vertaalde_letters = []
    for item in letters:
        if item == ' ':
            vertaalde_letters.append(' ')
        elif item not in morse_dictionary:
            vertaalde_letters.append('?')

        else:
            item_1 = morse_dictionary[item]
            vertaalde_letters.append(item_1)

    morse_Woord = ''.join(vertaalde_letters)

    print(morse_Woord)
    if '?' not in vertaalde_letters:
        None
    else: print("een ? duidt op een onvertaalbaar teken of een hoofdletter!")

vertaal_tekst_in_morse(woord = input)


