def show_exceptions():
    som = 0
    fo = None
    try:
        bestandsnaam = input("Geef bestandsnaam ")
        fo = open(bestandsnaam)

        line = fo.readline()
        while line != "":
            try:

                print(line)
                som =+ int(line)
                line = fo.readline()
            except ValueError as ex:
                print("er zit foutieve data in het bestand")
                print(ex)
                line = fo.readline()
        print("Einde try")

    except FileNotFoundError as ex:
        print("bestand bestaat niet")
        print(ex)
    except Exception as ex:
        print(ex)
    finally: #deze code wordt altijd uitgevoerd
        if fo != None:
            fo.close()
        print("bestand sluiten")

show_exceptions()