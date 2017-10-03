# # getal1= int(input('geef een geheel getal op : '))
# # getal2= int(input('geef een geheel getal op : '))
# # if(getal1 == getal2):
# #      print('getal {0} is gelijk aan {1}'.format(getal1,getal2))
# #  else: print("de getallen zijn verschillend")
#
# #Oefening 2: Even/Oneven
#
# # getal=float(input("geef een GEHEEL getal op"))
# # if getal%2==0:
# #     print("{0} is even".format(getal))
# # else: print("{0} is oneven".format(getal))
#
# #Oefening 3: Geboortejaar
#
# # print(input.__doc__)
# # import datetime
# # datum = datetime.datetime.now().date()
# # print(datum)
# print(input.__doc__)
# import datetime
# datum=datetime.datetime.now().year
#
# geboortejaar = int(input("geef je geboortejaar op: "))
# leeftijd = datum-geboortejaar
#
# if (leeftijd>=18):
#     print("Je mag alcohol drinken")
# else: print("Je bent nog geen 18, kom volgend jaar nog eens terug...")


# oefening 4: Hondenjaren
Leeftijd_Hond= int(input("Geef de leeftijd van uw hond op "))

Hondenjaren= (22+ (Leeftijd_Hond- 2)*5)

if (Leeftijd_Hond >= 3):
    print ("Deze leeftijd komt overeen met {0} mensenjaren".format(Hondenjaren))

if (Leeftijd_Hond == 2):
    print("Uw hond is 22 jaar oud")
if (Leeftijd_Hond == 1):
    print ("Uw hond is 14 jaar oud")
if (Leeftijd_Hond == 0):
    print ("dit kan niet. lol")
    