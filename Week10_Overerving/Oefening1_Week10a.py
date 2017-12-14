from Week10_Overerving.demo.demo.model_oef1.Ouder import Ouder
from Week10_Overerving.demo.demo.model_oef1.Student import Student

o1 = Ouder("pol", "put", 1949)
print(o1)

s1 = Student("An", "put",1,"NMCT", 1999)
s2 = Student("Miet", "put",2, "Devine", 1998)

o1.voeg_student_toe(s1)
o1.voeg_student_toe(s2)


print(o1.geef_info_studenten())
print(o1.geef_opleiding_studenten())