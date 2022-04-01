from abc import ABC,abstractmethod

class Emp(ABC):
    def __init__(self,id,nm,bs):
        self.eid = id
        self.ename = nm
        self.basic = bs

    def __str__(self):
        data = "Eid="+str(self.eid)
        data += "\nEname="+str(self.basic)
        data += "\nBasic="+str(self.basic)

        return data

    @abstractmethod
    def CalSal(self): #Abstract method = a method which has no defination(method without body)
        pass
        '''print("i am calsal from emp")
        return self.basic'''

# e1 = Emp(111,"EEE",23000)
# print(e1)
# e1.CalSal()

# if class has an abstract method then we cannot create object of that class
# ABC = abstract base class
# abstract class content abstract method (should not allow to create object)
