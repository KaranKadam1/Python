from programmer import Programmer
from admin import Admin
from salesmgr import Salesmgr

p1 = Programmer(111,"ppp",20000,200,2000)
s1 = Salesmgr(222,"sss",30000,3000)
a1=Admin(333,"AAA",40000,4000)

p1.display()
s1.display()
a1.display() 

allEmp = [p1,a1,s1]

for emp in allEmp:
    # p1.display,a1.display,s1.display,
    # polymorphic statement ->single message multiple implementation
    emp.display()