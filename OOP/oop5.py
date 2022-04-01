class Emp:
    # def __init__(self):
    #     self.eid = 100
    #     self.ename = "karan"
    #     self.basic = 12000
    
    # default argument concept
    def __init__(self,id=123,nm="karan",bs=200000):
        print("I am the constructor")
        self.eid = id
        self.ename = nm
        self.basic = bs
    
    def GetData(self):
        self.eid = int(input("Enter eid="))
        self.ename = input("Enter name=")
        self.basic = int(input("Enter basic="))


    def ShowData(self):
        print("eid = {0}".format(self.eid))
        print("ename = {0}".format(self.ename))
        print("basic = {0}".format(self.basic))

e1 = Emp()
e1.ShowData()

e2 = Emp(102,'Seema',33000)
e2.ShowData()




