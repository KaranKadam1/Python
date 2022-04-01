from emp import Emp

class EmpMgmt:
    def addEmp(self,e):
        # open the file for append
        fp = open("empData.txt","a")
        fp.write(str(e))
        fp.write("\n")
        fp.close()


    def showAllEmp(self):
        try:
            fp = open("empData.txt","r")
        except FileNotFoundError:
            print("file is not present")
        else:
            data = fp.read()
            print(data)
            fp.close()


    def searchEmpById(self,id):
        # opening file for reading
        with open("empData.txt","r") as fp:
            for line in fp:
                try:
                    # we need to search id in first 3 places
                    # if present in dsalary it shouldnt match
                    line.index(str(id),0,3)
                except:
                    pass
                else:   
                    print("Record Found..")
                    print(line)
                    break
            else:
                print("Record not Found..")


    def searchEmpByName(self,name):
        found = False
        with open("empData.txt","r") as fp:
            for line in fp:
                if(name in line):   
                    found = True
                    print(line.strip()) #strip method removes extra spaces and /n

        if(found == False):
            print("Record not Found..")


    def editEmpById(self,id):
        myEmp = []
        found = False
        with open("empData.txt","r") as fp:
            for line in fp:
                try:
                    line.index(str(id),0,3)
                except:
                    # no math
                    myEmp.append(line)  
                else:
                    # there is match(record found)
                    found = True
                    line = line.split(",")
                    ans = input("do you wish to change the name=")
                    if(ans.lower()=="y"):
                        line[1] = input("enter new name=")
                    ans = input("do you wish to change the salary=")
                    if(ans.lower()=="y"):
                        line[2] = input("enter new salary=")
                    line = ",".join(line)
                    line += "\n"
                finally:
                    myEmp.append(line)
        print(myEmp)           
        # # record found,so perform overwrite
        if found:
            with open("empData.txt","w") as fp:
                for emp in myEmp:
                    fp.write(emp)
        else:
            print("Record not found..")

        
    
    def deleteEmpById(self,id):
        myEmp = []
        found = False
        with open("empData.txt","r") as fp:
            for line in fp:
                try:
                    line.index(str(id),0,3)
                except:
                    # no math
                    myEmp.append(line)  
                else:
                    # there is match(record found)
                    found = True
        print(myEmp)           
        # record found,so perform overwrite
        if found:
            with open("empData.txt","w") as fp:
                for emp in myEmp:
                    fp.write(emp)
        else:
            print("Record not found..")


