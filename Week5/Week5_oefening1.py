# Maak volgende tuples aan:
# - tuple1 met de elementen 1NMCT, 2NMCT, 3NMCT
# - tuple2 met de elementen 1Devine, 2Devine, 3Devine
# - tuple3 met elementen van verschillende datatypes: “test”, True, 3.2 , 1
# Geef een antwoord op onderstaande vragen dmv een kort codevoorbeeld op bovenstaande
# tuples:
# - Wat is het effect als we in een tuple een element op een bepaalde positie willen wijzigen
# of verwijderen?
#Tuple does not support item assignments
# - Kan je op een tuple de methodes insert/append (zoals bij List) gebruiken?
#Tuple object has no attribute append/insert
# - Kan je via de plus-operator een tuple bij een andere tuple voegen?
#Ja
# - Kan je de vermenigvuldigingsoperator op een tuple gebruiken?
#Ja

tuple1 = ("1NMCT", "2NMCT", "3NMCT")
tuple2 = ("1Devine", "2Devine", "3Devine")
tuple3 = ("test", True, 3.2, 1)
#tuple1 [1] = [2]
#tuple3.append("Lies")
#tuple2.insert("lol")
tuplesum = tuple2 + tuple3
print (tuplesum)
tuplemulti = tuple2 * 8
print(tuplemulti)