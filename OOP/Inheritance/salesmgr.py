from emp import Emp

class Salesmgr(Emp):
    def __init__(self,id,nm,bs,incen):
    
        super().__init__(id,nm,bs)
        # print("i am Salesmgr class constructor")
        self.incentive = incen

    def __str__(self):
        data = super().__str__()
        data += "\nIncentive = "+str(self.incentive)
        return data

    def display(self):
        super().display()
        print("incentive= {0}".format(self.incentive))

'''s1 = Salesmgr(121,"kajal",40000,4500)
s1.displaySales()'''

