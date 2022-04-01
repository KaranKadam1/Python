from emp import Emp

class Programmer(Emp):
    def __init__(self, id, nm, bs,eh,cph):
        super().__init__(id, nm, bs)
        self.extraHrs = eh
        self.costPerHrs = cph

    def __str__(self):
        data = super().__str__()
        data += "\nExtraHrs="+str(self.extraHrs)
        data += "\nCost Per Hrs="+str(self.costPerHrs)
        return data
    
    def CalSal(self):
        # return super().CalSal() + self.extraHrs*self.costPerHrs
        return self.basic + self.extraHrs*self.costPerHrs
        
p1 = Programmer(111,"ppp",20000,20,2000)
print(p1)

# Def f1:
# pass
