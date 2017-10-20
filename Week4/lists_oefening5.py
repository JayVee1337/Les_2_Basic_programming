# Maak één list aan met de dagen van de week.
# Gebruik het printcommando in één codelijn volgende af te printen:
#  enkel de werkdagen van de week
#  de weekenddagen van de week
#  de onpare dagen van de week
#  de pare dagen van de week
dagen_van_de_week = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]
# def werkdagen(lijst):
#     lijst.pop(5)
#     lijst.pop()
#     print(lijst)
# def pare_dagen(lijst):
#     lijst.pop(0)
#     lijst.pop(1)
#     lijst.pop(2)
#     lijst.pop()
    #Als ik één ding pop verandert de lijst direct, daarm zijn de indexen zo raar :)

    # print(lijst)

def onpare_dagen(lijst):
    lijst.pop(1)
    lijst.pop(2)
    lijst.pop(3)
    print(lijst)

# werkdagen(dagen_van_de_week)
# pare_dagen(dagen_van_de_week)
onpare_dagen(dagen_van_de_week)
