from emp import Emp

class Admin(Emp):
    def __init__(self,id,nm,bs,comm):
    
        super().__init__(id,nm,bs)
        # print("i am Admin class constructor")
        self.commission = comm

    def __str__(self):
        data = super().__str__()
        data += "\nCommision = "+str(self.commission)
        return data

    def display(self):
        super().display()
        print("Commision= {0}".format(self.commission))

'''a1 = Admin(111,"Smitha",30000,5200)
a1.displayAdmin()'''

