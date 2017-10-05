voornaam= input("voornaam")
naam= input  ("naam")

def printGegevens (naam, voornaam, richting = "nmct"):
    print ("Naam is {0} voornaam is {1} en de richting is {2}".format(naam, voornaam, richting))

printGegevens(naam, voornaam)