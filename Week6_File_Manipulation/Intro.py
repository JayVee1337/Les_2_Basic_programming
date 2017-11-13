bestand = open("Demo", 'w+')

print(bestand)
bestand.write("Hallo NMCT!\n")
bestand.write("Hoe is het vandaag?\n")
bestand.write("Met mij goed, dank u!\n")
#niet vergeten
bestand.close()

bestand = open ("Demo",'r') #bestand inlezen

#print(bestand.readline())

lijn = bestand.readline().rstrip('\n')
while lijn != '':
    print(lijn)
    lijn = bestand.readline().rstrip('\n')

bestand.close()

bestand = open("Demo",'a+')
bestand.write("nog een lijn\n")

#cursor terug op begin plaatsen
bestand.seek(0)

print(bestand.readlines())
bestand.close()