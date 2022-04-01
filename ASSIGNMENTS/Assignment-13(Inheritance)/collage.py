'''
4. Create a class College which has collection of students. Add the 
following methods :
    a. Parameteried constructor for number of students.
    b. AddStudent
    c. GetStudent
    d. RemoveStudent
    e. Override __str__ Method
'''
from enggstud import EnggStudent
from Medstudent import MedicalStudent
from student import Student

class Collage(Student):
    def __init__(self, sid, nm, ag, pc):
        super().__init__(sid, nm, ag, pc)
        s1 = Student()
        
        p1 = EnggStudent()
        p1.display()
        m1 = MedicalStudent()
        m1.display()
        allstud = [s1,p1,m1]
        print(allstud)

