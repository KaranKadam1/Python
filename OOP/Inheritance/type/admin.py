from emp import Emp

class Admin(Emp):
    def __init__(self, id, nm, bs,comm):
        super().__init__(id, nm, bs)
        self.commmision = comm
    
    def __str__(self):
        data = super().__str__()
        data += "\nCommision="+str(self.commmision)
        return data
    
    def CalSal(self):
        # return super().CalSal() + self.commmision
        return self.basic + self.commmision