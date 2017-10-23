lijst = ["aap", "beer", "flamingo"] #list dynamische sequentie
print(lijst)
tup = ("zaterdag", "zondag") #statisch
print(tup[0])
#tup(0)= "vrijdag" gaat niet!!

set_list = {"palm", "kriek", "duvel", "orval", "duvel"}
print((set_list))
#List met accolades{} negeert dupes!!! = Set_list is wel dynamisch
set_list.add("omer")
set_list.add("cara")
set_list.add("cara")
print(set_list)
#Geen bepaalde positie in Set_list (geen index)

#Bij dictionary kan je alle datatypes toepassen
dict = {0:"pol",1:"bert",2:"Miet",3:"Ludwig",3:"An"}
print(dict)
print(dict[0])
dict[1] = "Pieter"
dict[4] = "Marie"
dict [5] ="Bert"
print(dict)
print(len(dict))
dict[len(dict)] = "Marcel"
print(dict)

for key in dict.keys():
    print(key)
    print(dict[key])
for value in dict.values():
    print (value)
for key,value in dict.items():
    print ("{0} : {1}".format(key, value))

if 10 in dict.keys():
    print(dict[10])
else: print("deze key bestaat niet")