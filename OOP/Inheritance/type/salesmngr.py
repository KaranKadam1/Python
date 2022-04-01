from emp import Emp

class Salesmngr(Emp):
    def __init__(self, id, nm, bs,incen):
        super().__init__(id, nm, bs)
        self.incentive = incen

    def __str__(self):
        data = super().__str__()
        data += "\nIncentive="+str(self.incentive)
        return data
    
    def CalSal(self):
        # return super().CalSal() + self.incentive
        return self.basic + self.incentive