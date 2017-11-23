from Week7.model.Oefening3_Week7_auto import Auto
import random

autos = []

polootje = Auto("geel", 'vw', 'benzine', 'polo', 2200)
corsaatje = Auto('roze', 'opel', 'mazout', 'corsa', 50000)
vijfhonderd = Auto('wit', 'fiat', 'benzine', 'cinquecento', 65512)

autos.append(polootje)
autos.append(corsaatje)
autos.append(vijfhonderd)

for auto in autos:
    aantalkm = random.randrange(20,400)
    auto.rijden(aantalkm)
    print(auto)