print ("hello git")
print ("how you doin")
print ("how you doin")

print ("how you doin")

print ("boi")

#commentaar 
totaal_seconden = int(input("geef het aantal seconden op: "))
aantal_dagen = totaal_seconden // 86400
rest1 = totaal_seconden % (24*60*60)
aantal_uren = rest1 // 3600
rest2 =  rest1 % 3600
aantal_minuten = rest2 // 60
rest3= rest2 % 60
aantal_seconden = rest3

print("het aantal dagen bedraagt %s.\n Het aantal uren bedraagt %s.\n Het aantal minuten bedraagt %s.\n Het aantal seconden bedraagt %s" % (aantal_dagen, aantal_uren, aantal_minuten, aantal_seconden))