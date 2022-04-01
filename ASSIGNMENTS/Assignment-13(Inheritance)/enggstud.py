'''
2. Create a derived class from Student as EnggStudent with :
    a. Data members as : 
        i. Branch
        ii. InternalMarks
    b. Add the following methods :
        i. Parameterized constructor
        ii. Display
        iii. Accept
        iv. override Method CalculateRank
        v. Override __str__ Method
'''
from student import Student

class EnggStudent(Student):

    def __init__(self, sid=0, nm="", ag=0, pc=0,bc="",im=0):
        self.Branch = bc
        self.InternalMarks = im
    
    def Accept(self):
        self.Branch = input("enter your branch=")
        self.InternalMarks = int(input("enter internal marks="))

    def __str__(self):
        data = super().__str__()
        data +="\n Branch="+str(self.Branch)
        data += "\n Internal Marks="+str(self.InternalMarks)
        return data
    
    def display(self):
        super().display()
        print("\n branch="+str(self.Branch))
        print("\n intmark="+str(self.InternalMarks))

    def rank1(self):
        super().rank()

p1 = EnggStudent()
p1.Accept()
# p1.display()

        
