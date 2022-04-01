'''
create a class with following:
a.data members:
        i.studentid
        ii.Name
        iii.Age
        iv.Percentage
b.Add the following methods:
        i.parameterized constructor
        ii.Display
        iii.Accept
        iv.Method CalculatorRank
        v.Override__str__Method
'''
class Student():

        def __init__(self,sid=0,nm="",ag=0,pc=0):
             self.sid = sid
             self.name = nm
             self.age = ag
             self.percentage = pc

        def display(self):
                print("Id={0}".format(self.id))
                print("name={0}".format(self.name))
                print("age={0}".format(self.age))
                print("percentage={0}".format(self.percentage))

        def getdata(self):
                self.id = int(input("enter id="))
                self.name = input("enter name=")
                self.age = int(input("enter age="))
                self.percentage = int(input("enter percentage="))

        def rank(self):
                if self.percentage>=90 and self.percentage<=100 :
                        print("First Rank")
                elif self.percentage>=70 and self.percentage<90:
                        print("Second Rank")
                elif self.percentage>=50 and self.percentage<70:
                        print("Third Rank")
                elif self.percentage>=40 and self.percentage<50:
                        print("Pass")
                elif self.percentage<40:
                        print("Fail")

        def __str__(self):
                data = "sid="+(self.sid)
                data += "\n name="+str(self.name)
                data += "\n age="+str(self.age)
                data += "\n percentage="+str(self.percentage) 
                return data

s1 = Student()
s1.getdata()
s1.display()
s1.rank()
