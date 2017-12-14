from Week9.Oefening3_Week9 import Bier
#nummer, naam, brouwerij, kleur, alcoholpercentage.
biertjes = []

bier1 = Bier( 32, 'lmao', 'brouwerij', 'groen', 98.0)
bier2 = Bier(563, 'Orval', '', 'blauw', 12.0)
bier3 = Bier(15, 'Jupiler', 'brouwerij', 'geel', 212)

biertjes.append(bier1)
biertjes.append(bier2)
biertjes.append(bier3)

for bier in biertjes:
    print(bier)