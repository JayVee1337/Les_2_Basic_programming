# Oef 01: Voeg een tekstbestand toe aan uw projectmap. Voorzie het tekstbestand van verschillende
# regels tekst. Maak nu een functie ‘lees_bestand_in_met_lijnnummers’ die het tekstbestand
# inleest en lijn per lijn afprint. Elke lijn wordt door een lijnnummer vooraf gegaan.
bestand=open("Oef1_6", 'w+')

bestand.write("The ting goes skrrraaa\n")
bestand.write("PAPAPAPA\n")
bestand.write("SKIBIDIPAPA\n")
bestand.write("And the BOOMBOOMDOBODOOMBOOM\n")
bestand.write("SKYAA")
bestand.close()


def lees_bestand_in_met_lijnnummers(bestand):
    bestand = open("Oef1_6", 'r')
    lijn = bestand.readline().rstrip('\n')
    index=0
    while lijn != '':
        index = index+1
        print("{0}.{1}".format(index, lijn))
        lijn= bestand.readline().rstrip('\n')
lees_bestand_in_met_lijnnummers(bestand)