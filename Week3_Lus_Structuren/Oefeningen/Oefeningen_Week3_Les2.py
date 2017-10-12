def swap(woord1, woord2, woord3, woord4, woord5):
    woord1 = str(input("geef een woord op"))
    woord2 = str (input("geef een ander woord op"))
    woord3= woord1 [:2] + woord2 [2:]
    woord4 = woord2[:2]  + woord1[2:]
    woord5 = woord3+woord4
    print (woord5)
swap(woord1 = input, woord2 = input, woord3 = str, woord4 = str, woord5 = str)