# Oefening  1 Werken Met Functie
# def printWelkom (naam = "Jens"):
#     print("Je naam is {0}".format(naam))
#
# printWelkom()

#Oefening 2
# naam = input("Geef Naam plis: ")
#
# def printWelkom(naam, groep = "nmct4"):
#     print("Je naam is {0} en je groep is {1}".format(naam,groep))
#
# printWelkom(naam)

#Oefening 3
# def printWiskunde (a,b,c=0,d=0):
#     Berekening = a-b+c-d
#     print("de uitkomst is {0}".format(Berekening))
#
# printWiskunde(2, 4)

#Oefening 4: Maximum
# def printMaximum(a, b, c):
#     if (a >= b) and (a >= c):
#         print("Het maximum is {0}".format(a))
#     elif (b >= a) and (b>= c):
#         print ("Het maximum is {0}".format(b))
#     elif (c >= a) and (c >= b):
#         print ("Het maximum is {0}".format(c))
# printMaximum (6532, 312, 643516543)

#Oefening 5: Maandnummer
maand = float(input("geef een maandnummer op "))
def maandNummer (maand):
    if (maand == 1):
        print ("Dit is de maand januari")
    elif (maand == 2):
        print ("Dit is de maand februari")
    elif (maand == 3):
        print ("Dit is de maand maart")
    elif (maand == 4):
        print ("Dit is de maand april")
    elif (maand == 5):
        print ("Dit is de maand mei")
    elif (maand == 6):
        print ("Dit is de maand juni")
    elif (maand == 7):
        print("Dit is de maand juli")
    elif (maand == 8):
        print("Dit is de maand augustus")
    elif (maand == 9):
        print("Dit is de maand september")
    elif (maand == 10):
        print("Dit is de maand oktober")
    elif (maand == 11):
        print("Dit is de maand november")
    elif (maand == 12):
        print("Dit is de maand december")
    elif (maand >= 13):
        print ("Dit is niet mogelijk!!")

maandNummer(maand)
