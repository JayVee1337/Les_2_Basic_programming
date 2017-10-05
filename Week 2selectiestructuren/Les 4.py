#lengte= 4
#breedte= 6
#
# #BerekenOppervlakteRechthoek () methode declareren voor je ze aanroept
# print ("lijn 8")
#functie schrijven
def BerekenOppervlakteRechthoek (lengte=0, breedte= 0):
    #alle statements met de tab indent behoren tot deze methode
    if(lengte == 0) and (breedte==0):
        lengte = int(input("geef de lengte "))
        breedte= int(input("geef de breedte "))
    Oppervlakte= lengte*breedte
    print("de oppervlakte is {0}".format(Oppervlakte))
    print ("de breedte is {0}".format(breedte))
BerekenOppervlakteRechthoek(3, 8)
BerekenOppervlakteRechthoek(8, 10)
BerekenOppervlakteRechthoek()