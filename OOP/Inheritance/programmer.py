from emp import Emp

# class ChildClass(ParentClass)
class Programmer(Emp):
    def __init__(self,id,nm,bs,eh,cph):
        # call the parent class constructor
        # super indicates parent class
        super().__init__(id,nm,bs)
        # print("i am programmer class constructor")
        self.extraHrs = eh
        self.costPerHrs = cph

    def __str__(self):
        data = super().__str__()
        data += "\nExtra Hrs = "+str(self.extraHrs)
        data += "\nCost Per Hrs = "+str(self.costPerHrs)
        return data

    def display(self):
        super().display()
        print("Extra Hrs={0}".format(self.extraHrs))
        print("Cost Per Hrs={0}".format(self.costPerHrs))

'''p1 = Programmer(101,"Karan",20000,20,200)
# p1.displayEmp()
p1.displayPrg()'''

