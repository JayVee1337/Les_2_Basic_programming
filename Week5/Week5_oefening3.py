# Oef03: Maak volgende 2 dictionaries aan.
# Ze stellen beide de verschillende studentenaantallen per opleidingsjaar voor.
# - ‘nmct’ met de elementen {"1NMCT": 101, "2NMCT": 88, "3NMCT": 77}
# - ‘devine’ met de {"1Devine": 123, "2Devine": 98, "3Devine": 55}
# Geef een antwoord op onderstaande vragen dmv een kort codevoorbeeld op bovenstaande
# dictionaries:
# - Wat is het effect van het print-commando op een dictionary?
#Het print elk element met zijn key af
# - Hoe kan je een element uit de dictionary opvragen?
#print(nmct[key]
# - Hoe voeg je een nieuw element aan een dictionary toe?
# .update ({})
# - Wat gebeurt er als een nieuw element met dezelfde key aan een dictionary toegevoegd
# wordt?
#Het nieuwe element vervangt het oude met dezelfde key
# - Hoe controleer je of een key in een dictionary reeds in gebruik is?
#  je kan de key proberen afprinten
# - Hoe kan je een key (met value) uit een dictionary verwijderen?
# del dict[key]
# Wat als key niet aanwezig is?
# keyerror
nmct = {"1NMCT":101, "2NMCT": 88, "3NMCT": 77}
devine = {"1Devine": 123, "2Devine": 98, "3Devine":  55}
print(nmct, devine)
print(nmct["1NMCT"])
nmct.update({"65411545631NMCT":6564151})
print(nmct)
nmct.update({"1NMCT":"1NMCT4FORLIFE"})
print (nmct)
print (nmct["1NMCT"])
del nmct["2NMCT"]
print(nmct)
del nmct[531]