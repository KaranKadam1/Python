class Emp:
    def __init__(self,id=100,nm="",bs=0):
        # print("i am emp class constructor")
        self.eid = id
        self.ename = nm
        self.basic = bs

    def __str__(self):
        data = "Eid = "+str(self.eid)
        data += "\nEname = "+self.ename
        data += "\nBasic ="+str(self.basic)
        return data

    def display(self):
        print("Eid = {0}".format(self.eid))
        print("Ename = {0}".format(self.ename))
        print("Basic= {0}".format(self.basic))
       
# e1 = Emp(101,"Karan",3400)
# e1.displayEmp()
# every data type is inherited from object class
# __str__ converts data into string
