from Week9.student import Student


def verwerk_studentenfile(bestandsnaam):
    return Student.lees__studenten_file_in(bestandsnaam)


studentenlijst = verwerk_studentenfile('student.csv')
for item in studentenlijst:
    print(item)