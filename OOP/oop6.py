class Student:    
    #Accept input from user
    def getData(self):
        self.sid = int(input("Enter student id"))
        self.sname = input("Enter student name")
        self.age = int(input("Enter student age"))
        self.percentage = float(input("Enter percentage"))

    def showData(self):
        print("Sid = {0}".format(self.sid))
        print("SName = {0}".format(self.sname))
        print("Age ={0}".format(self.age))
        print("Percentage ={0}".format(self.percentage))


#Create object

s1 = Student()
s1.getData()
s1.showData()
    
