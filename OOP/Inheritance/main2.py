from programmer import Programmer
from admin import Admin
from salesmgr import Salesmgr

p1 = Programmer(111,"ppp",20000,200,2000)
s1 = Salesmgr(222,"sss",30000,3000)
a1=Admin(333,"AAA",40000,4000)

# print(p1) #str method from object will be called 
# print(str(p1))
allEmp = [p1,a1,s1]
for emp in allEmp:
    print(emp)#str(p1),(a1),(s1)

