#from filename import classname
from emp import Emp

allEmp = {}
choice = 0
while(choice!=7):
    print('''\t\t1.Add Emp
        \t\t2.Show all Emp
        \t\t3.Edit Emp
        \t\t4.Delete Emp
        \t\t5.Search Emp by id
        \t\t6 Search EMP by name
        \t\t7.Exit''')

    choice = int(input("Enter your choice="))
    
    if(choice == 1):
        nm = input("Enter name of emp=")
        bs = float(input("Enter basic salary="))
        e1 = Emp(nm,bs)
        allEmp[e1.eid] = e1
        
    elif(choice == 2):
        #print(allEmp)
        for emp in allEmp.values():
            print("----------------------")
            emp.showEmp()
    
    elif(choice == 3):
        id = int(input("Enter eid which you want to edit="))
        if(id in allEmp):
            ans = input("Do you want to change name(y/n)?")
            if(ans.lower() == "y"):
                name = input("enter new name=")
                allEmp[id].ename = name
            ans = input("Do you want to change salary(y/n)?")
            if(ans.lower() == "y"):
                basic = float(input("enter new basic="))
                allEmp[id].basic = basic
        else:
            print("Emp not present")

    elif(choice == 4):
        id = int(input("Enter eid which you want to delete="))
        if(id in allEmp):
            allEmp.pop(id)
            print("Emp deleted ...")
        else:
            print("Emp not present")

    elif(choice == 5):
        id = int(input("Enter eid="))
        if(id in allEmp):
            print("This emp is present")
            allEmp[id].showEmp()
        else:
            print("this emp is not present")
    
    elif(choice == 6):
        name = input("Enter name=")
        # .values will return object
        for emp in allEmp.values():
            if(name == emp.ename):
                print("Emp found")
                emp.showEmp()
                break
        else:
            print("Emp not found")

    


        