class Emp:
    def __init__(self):
        self.eid = 100
        self.ename = "karan"
        self.basic = 12000
    def GetData(self):
        self.eid = int(input("Enter eid="))
        self.ename = input("Enter name=")
        self.basic = int(input("Enter basic="))

    def ShowData(self):
        print("eid = {0}".format(self.eid))
        print("ename = {0}".format(self.ename))
        print("basic = {0}".format(self.basic))

e1 = Emp()
e1.ShowData() #shows constructor values
e1.GetData()
e1.ShowData()

