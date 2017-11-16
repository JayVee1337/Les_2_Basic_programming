# Oef03: Maak de functie ‘vul_bestand_aan’. Deze functie is analoog als de vorige functie
# ‘schrijf_input_naar_bestand’ behalve dat het bestand onderaan verder aangevuld wordt (en
# de bestaande inhoud dus niet gewist wordt). Test uit.


def vul_bestand_aan(bestandsnaam):

    test2= open(bestandsnaam, 'w+')
    lijn = input("geef een nieuwe lijn in, om af te sluiten voer je s in ")
    while lijn != 's':
        test2.write(lijn + '\n')
        lijn = input("geef een nieuwe lijn in, om af te sluiten voer je s in ")
    test2.close()


filename = "test2"
vul_bestand_aan(filename)
