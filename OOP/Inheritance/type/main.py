from programmer import Programmer
from admin import Admin
from salesmngr import Salesmngr

p1 = Programmer(111,"ppp",20000,20,2000)
s1 = Salesmngr(222,"sss",30000,3000)
a1 = Admin(333,"AAA",40000,4000)

allEmp = [p1,a1,s1]

for emp in allEmp:
    print("-------------------------")
    print(emp)
    print("Total Salary = ",emp.CalSal())
