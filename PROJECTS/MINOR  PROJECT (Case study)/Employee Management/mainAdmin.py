from empMgmt import EmpMgmt
from emp import Emp

def admin():
    empMgmt = EmpMgmt()
    choice = 0
    
    while(choice != 10):
        print('''\t1.Add Emp
            2.Show all Emps
            3.search Emp by id
            4.search Emp by name
            5.delete emp by id
            6.edit emp by id
            10.Exit''')

        choice = int(input("Enter your choice:"))
    
        if(choice == 1):
            id = int(input("enter emp id="))
            nm = input("enter emp name=")
            bs = float(input("enter basic salary="))
            e1 = Emp(id,nm,bs)
            # Add this emp to file
            empMgmt.addEmp(e1)
        
        elif(choice == 2):
            empMgmt.showAllEmp()

        elif(choice == 3):
            id = int(input("enter emp id to search="))
            empMgmt.searchEmpById(id)
        
        elif(choice == 4):
            name = input("enter emp name to search=")
            empMgmt.searchEmpByName(name)
        
        elif(choice == 5):
            id = int(input("enter emp id to delete="))
            empMgmt.deleteEmpById(id)

        elif(choice == 6):
            id = int(input("enter emp id to edit="))
            empMgmt.editEmpById(id)

if __name__ == '__main__':
    admin()