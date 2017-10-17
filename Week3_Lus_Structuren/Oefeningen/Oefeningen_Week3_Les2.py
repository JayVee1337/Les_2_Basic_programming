# # #Oefening 1 = Vens Jercauteren
# def swap(woord1, woord2, woord3, woord4, woord5):
#     woord1 = str(input("geef een woord op"))
# # Zet een spatie voor maximaal effect!
#     woord2 = str (input("geef een ander woord op"))
#     woord3= woord1 [:2] + woord2 [2:]
#     woord4 = woord2[:2]  + woord1[2:]
#     woord5 = woord4+woord3
#     print (woord5)
# swap(woord1 = input, woord2 = input, woord3 = str, woord4 = str, woord5 = str)


# # Oefening 2: genereer paswoord
# def genereer_paswoord (naam, voornaam, datum, paswoord, voornaam_Upper, naam_Lower):
#     Naam = str(input("geef uw naam op(zonder spatie) "))
#     voornaam = str (input ("geef uw voornaam op(zonder spatie) "))
#     datum = input("geef de datum op in het format dd-mm-yyyy(zonder spatie) ")
#     voornaam_Upper = voornaam.upper()
#     naam_Lower = Naam.lower()
#     paswoord = naam_Lower[:3]+ voornaam_Upper[:2] + datum [3:5] + datum [8:10]
#     print (paswoord)
# genereer_paswoord(naam = str, voornaam = str, datum = str, paswoord=str, voornaam_Upper=str, naam_Lower=str)
#

# Oefening 3: Howest e-mail (Te Moeilijk)

#1) @student.howest.be erin?
#2) punt aanwezig?
#3) enkel a-z 1-9
#4)minstens 2 karakters voor naam en voornaam

# def Controle_Howest_email(mailadres):
#     pos = mailadres.find(("@student.howest.be"))
#     if pos == -1:
#         return False
#         print(("lelijk"))
#     voornaam_naam = mailadres[:pos] #wegknippen @student.howest.be
#     #controle punt
#
#     #controle van a-z / 1-9
#     if (str.isalnum == True):
#         return True
#     else: return False
#     return True
# if Controle_Howest_email(str(input)):
#     print("Correct email adres")
# else: ("Dit is niet het juiste soort email adres")
#
# Controle_Howest_email(mailadres= "Jens.Vercauteren@t")

#Oefening4: Password-Generator

import random

def Random_Password(Maximum_Lengte, Minimum_Lengte, Gekozen_Lengte):
    Maximum_Lengte = int(input("Geef de maximumlengte van uw wachtwoord "))
    Minimum_Lengte = int(input("Geef de minimumlengte van uw wachtwoord"))
    Gekozen_Lengte = random.randrange(Minimum_Lengte,Maximum_Lengte,[1])
    print(Gekozen_Lengte)
Random_Password(Minimum_Lengte=float, Maximum_Lengte=float, Gekozen_Lengte=float)