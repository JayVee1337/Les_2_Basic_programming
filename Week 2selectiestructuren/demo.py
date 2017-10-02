# # # print("test")
# # # Om dingen snel in commentaar te zetten: Selecteren en dan ctrl+deelteken!
# # # naam = input("geef naam")
# # # voornaam = input("geef voornaam")
# # # print ("voornaam is: {0:10s} en de naam is {1}".format(voornaam, naam))
# # #10s zorgt ervoor dat er zeker 10 plaatsen worden overgehouden voor de voornaam (MINSTENS)
# # x=4/3
# # #een getal van 5 digits en 2 cijfers na de komma
# # print("een mottig getal {0:5.2f}".format(x))
# #x = input("geef een getal")
# # print("een mottig getal {0:5.2f}".format(x))
# #dit werkt niet omdat input zorgt voor een string en geen float
# #oplossing:
# # x =float(input("geef een getal"))
# # print("een mottig getal {0:5.2f}".format(x))
#
# totaal_seconden = int(input("geef het aantal seconden op: "))
# aantal_dagen = totaal_seconden // 86400 #het aantal volledige dagen
# rest1 = totaal_seconden % (24*60*60)
# aantal_uren = rest1 // 3600 #Het aantal volledige uren
# rest2 =  rest1 % 3600
# aantal_minuten = rest2 // 60
# aantal_seconden = rest2 % 60
#
# print("het aantal dagen bedraagt {0}.\n Het aantal uren bedraagt {1}.\n Het aantal minuten bedraagt {2}.\n Het aantal seconden bedraagt {3}".format(aantal_dagen, aantal_uren, aantal_minuten, aantal_seconden))

import math
print(math.pi)

print(input.__doc__)
import datetime
datum = datetime.datetime.now().date()
print(datum)
