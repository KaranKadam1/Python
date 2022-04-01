class Emp:
    def __init__(self,id=0,nm="",bs=0):
        self.eid = id
        self.ename = nm
        self.basic = bs

    def __str__(self):
        data=""
        data = str(self.eid)+","+self.ename+","+str(self.basic)
        return data
