from Week9.Week9_Oefening2 import Bier
#nummer, naam, brouwerij, kleur, alcoholpercentage.
biertjes = []

bier1 = Bier( 32, 'lmao', 'brouwerij', 'groen', 98.0)
bier2 = Bier(563, 'Orval', '', 'blauw', 12.0)
bier3 = Bier(15, 'Jupiler', 'brouwerij', 'geel', 14.0)

biertjes.append(bier1)
biertjes.append(bier2)
biertjes.append(bier3)

for bier in biertjes:
    print(bier)