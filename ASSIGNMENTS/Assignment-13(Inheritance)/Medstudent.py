'''
3. Create a class MedicalStudent inherited from Student with following :
    a. Data members :
       i. Specialization
       ii.MarksOfInternship

    b. Add the following methods :
       i. Parameterized constructor
       ii. Display
       iii. Accept
       iv. override Method CalculateRank
       v. Override __str__ Method

'''
from student import Student

class MedicalStudent(Student):
    def __init__(self, sid=0, nm="", ag=0, pc=0,sp="",moi=0):
        super().__init__(sid, nm, ag, pc)
        self.Specialization = sp
        self.MarksOfInternship = moi

    def Accept(self):
        self.Specialization = input("Enter a specialization=")
        self.MarksOfInternship = int(input("enter marksofinternship="))

    def __str__(self):
        data = super().__str__()
        data +="\n specialization = "+str(self.Specialization)
        data +="\n marksofinternship= "+str(self.MarksOfInternship)
        return data

    def display(self):
        #super().display()
        print("\n specialization in:{0}".format(self.Specialization))
        print("\n marksofinternship are:{0}".format(self.MarksOfInternship))

    def rank2(self):
        super().rank()

m1 = MedicalStudent()
m1.Accept()
# m1.display