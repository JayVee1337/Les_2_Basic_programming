# Maak een lege list ‘nieuwe_list_getalllen’ aan.
# Vul deze list op met getallen startend vanaf 1, met stapgrootte 23, tem 484.
# Vervolgens:
#  Print de list af.
#  Print de list in omgekeerde volgorde af.
#  Verwijder het eerste element en print opnieuw de list af.
#  Zoek de werkwijze om een specifiek element uit de list te verwijderen.
#  Hoe kan je op eenvoudige wijze het laatste element uit de list afprinten?
Nieuwe_list_getallen = []

def vul_lijst_op(lijst):
    for getal in range(1,485,23):
        lijst.append(getal)
    #pop met index verwijdert dat specifieke element, gewoon pop() verwijdert het laatste element
    lijst.pop()
    print(lijst)

def print_lijst(lijst):
    for item in lijst:
        print(item)

def print_lijst_omgekeerd(lijst):
    aantal = len(lijst)
    for item in range(aantal-1, -1, -1):
        print(lijst[item])





# def print_omgekeerd(lijst):
#     #Draait lijst om, en dat is niet de opgave
#     for i in reversed(Nieuwe_list_getallen):
#         print(i)
# vul_lijst_op(Nieuwe_list_getallen)
# print_lijst(Nieuwe_list_getallen)
# print_lijst_omgekeerd(Nieuwe_list_getallen)
vul_lijst_op(Nieuwe_list_getallen)