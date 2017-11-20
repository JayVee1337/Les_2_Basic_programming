from Week7.Oefening1_Week7 import Boek

boek1 = Boek("Percy Jackson and the sea of monsters", 'Rick Riordan', 250, "paperback", "science fiction")
boek2 = Boek("The Spook's Apprentice: The Spook's Revenge",'Joseph Delaney', 354, "paperback", "fictional medieval adventure")
boek3 = Boek("A second chance at Eden", "Peter F. Hamilton", 512, "paperback", "futuristic science fiction")
boeken = []
boeken.append(boek1)
boeken.append(boek2)
boeken.append(boek3)
for boek in boeken:
    print(boek)