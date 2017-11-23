from Week7.Oefening5_Week7 import Winkelkar

delhaize = Winkelkar()
colruyt = Winkelkar()

delhaize.voeg_product_toe('brood')
delhaize.voeg_product_toe('melk')
delhaize.voeg_product_toe('hesp')
delhaize.voeg_product_toe('kaas')
colruyt.voeg_product_toe('cara')

print(delhaize)

delhaize.verwijder_product('melk')

print(delhaize)
print(colruyt)

volledige_kar = delhaize + colruyt
delhaize+=colruyt

print(volledige_kar)
print(delhaize)
