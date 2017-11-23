from Week7.Student import Student

#We maken een object met referentie student1 van de klasse Student
#Via Student(naam, voornaam) wordt de init methode van de klasse student aangeroepen
#self verwijst naar zichzelf en is altijd noodzakelijk
student1 = Student ('Put', 'Pol', 'man', 25)

print(student1)
print(student1.naam)
print(student1.voornaam)
student1.naam = "Vandenberghe"
print (student1.naam)

student2 = Student('Flouw', 'Romuald', 'iets tussen man en vrouw', 100)
studenten = []
studenten.append(student1)
studenten.append(student2)
print(studenten)

student2.naam = 'Flouw'

for student in studenten:
    print(student)

    print("naam is {0} en voornaam is {1}, hij is {2} en {3} jaar oud".format(student.naam, student.voornaam, student.geslacht, student.leeftijd))
