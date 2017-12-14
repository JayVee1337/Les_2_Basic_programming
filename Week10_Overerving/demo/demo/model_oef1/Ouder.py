from Week10_Overerving.demo.demo.model_oef1.Persoon import Persoon
from Week10_Overerving.demo.demo.model_oef1.Student import Student
class Ouder(Persoon):
    def __init__(self, naam, voornaam, geboortejaar):
        super().__init__(naam, voornaam, geboortejaar)
        self.__studenten = []

    def __str__(self):
        return "Ouder {0}".format(super().__str__())

    @property
    def studenten(self):
        return self.__studenten

    def voeg_student_toe(self, stud):
        if isinstance(stud, Student):
            if stud not in self.__studenten:
                self.__studenten.append(stud)
        else:
             raise ValueError("Geen geldige student!!!")


    def geef_info_studenten(self):
        info = ""
        for stud in self.studenten:
            info += str(stud) + "volgt de opleiding " + stud.opleiding + "\n"

        info += str(self)
        return info


    def geef_opleiding_studenten(self):
        opleidingen = []
        for stud in self.studenten:

            opleidingen.append(Student.opleiding)

        return opleidingen

    def __repr__(self):
        return repr(Student.opleiding)
