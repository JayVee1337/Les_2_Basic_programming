# getal1= int(input('geef een geheel getal op : '))
# getal2= int(input('geef een geheel getal op : '))
# if(getal1 == getal2):
#      print('getal {0} is gelijk aan {1}'.format(getal1,getal2))
#  else: print("de getallen zijn verschillend")

#Oefening 2: Even/Oneven

# getal=float(input("geef een GEHEEL getal op"))
# if getal%2==0:
#     print("{0} is even".format(getal))
# else: print("{0} is oneven".format(getal))

#Oefening 3: Geboortejaar

# print(input.__doc__)
# import datetime
# datum = datetime.datetime.now().date()
# print(datum)
print(input.__doc__)
import datetime
datum=datetime.datetime.now().year

geboortejaar = int(input("geef je geboortejaar op: "))
leeftijd = datum-geboortejaar

if (leeftijd>=18):
    print("Je mag alcohol drinken")
else: print("Je bent nog geen 18, kom volgend jaar nog eens terug...")

