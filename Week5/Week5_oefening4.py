# 4: Maak nu één functie ‘print_dictionary’ die de verschillende elementen overloopt waarbij
# telkens key & value samen op één lijn worden afgeprint.
# De functie heeft als parameters een naam (voor de dictionary) en de dictionary zelf.
# Voorbeeld:

def print_dictionary (dict, naam):
    print ("voor de verzameling {0}: ". format(naam))
    for key,value in dict.items():
        print ("key: {0} --> Value: {1}".format(key, value))

nmct = {"1NMCT":1, "2NMCT":2, "3NMCT":3}
devine= {"1Devine":1 ,"2Devine":2, "3Devine":3}

print_dictionary(nmct,  "NMCT")