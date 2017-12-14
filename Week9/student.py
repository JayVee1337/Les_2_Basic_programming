#naam;leeftijd;
class Student:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        self.__naam = value

    @property
    def leeftijd(self):
        return self.__leeftijd

    @leeftijd.setter
    def leeftijd(self, value):
        if isinstance(value, int) and value >= 16:
            self.__leeftijd = value
        else:
            self.__leeftijd = None
            raise ValueError("student is te jong of leeftijd is onbekend")

    def __repr__(self):
        return ("de naam is {0} en hij/zij is {1} jaar oud".format(self.naam, self.leeftijd))

    def __str__(self):
        return ("de naam is {0} en hij/zij is {1} jaar oud".format(self.naam, self.leeftijd))

    @staticmethod#gemeenschappelijke klasse methode
    def lees__studenten_file_in(bestandsnaam):
        studenten = []
        fo = open(bestandsnaam, 'r')
        lijn = fo.readline() #eerste lijn (titel) mag weg
        lijn = fo.readline()
        while lijn != "":
            try :
                delen = lijn.split(';') #ik krijg list met data van de verschillende kolommen
                student = Student(delen[0],int (delen[1]))
                studenten.append(student)

            except IndexError as ex:
                print("onvolledige student : {0}".format(lijn))
            except ValueError as ex:
                print(ex)
            finally:
                lijn = fo.readline()
        fo.close()
        return studenten
