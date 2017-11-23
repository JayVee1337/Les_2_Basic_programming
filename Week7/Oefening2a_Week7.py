from Week7.Oefening2_Week7 import Bier
#nummer, naam, brouwerij, kleur, alcoholpercentage.
biertjes = []

bier1 = Bier(6454, 'Duvel', 'brouwerij', 'groen', 1531)
bier2 = Bier(563, 'Orval', '', 'blauw', 12)
bier3 = Bier(15, 'Jupiler', 'brouwerij', 'geel', 5615315315651)

biertjes.append(bier1)
biertjes.append(bier2)
biertjes.append(bier3)

for bier in biertjes:
    print(bier)