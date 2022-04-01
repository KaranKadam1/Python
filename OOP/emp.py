class Emp:

    count = 100
    def __init__(self,nm,bs):

        Emp.count += 1
        self.eid = Emp.count  #generating id to avoid dupplicate ids
        self.ename = nm
        self.basic = bs
    
    def showEmp(self):
        print("Eid={0}".format(self.eid))
        print("Ename={0}".format(self.ename))
        print("Basic={0}".format(self.basic))
