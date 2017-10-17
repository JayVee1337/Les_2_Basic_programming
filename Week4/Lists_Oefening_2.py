vrienden = []

def lijst_vrienden_aanvullen():
    add = str
    while add != "":
        add = (input("Geef de naam van een vriend op, of sluit af met een leeg veld: "))
        vrienden.append(add)
        if add == "":
            vrienden.remove("")

    print("Uw vrienden zijn: {0}".format(vrienden))


lijst_vrienden_aanvullen()
