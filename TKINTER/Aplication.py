from tkinter import *
from tkinter import messagebox


def ClearData():
    txEid.delete(0,END)
    txEname.delete(0,END)
    txBasic.delete(0,END)
    txBasic.delete(0,END)
    txEid.focus()  #for curser

def addEmp():
    eid = txEid.get()
    ename = txEname.get()
    basic = txBasic.get()
    emp = eid+","+ename+","+basic
    listEmp.insert(END,emp)
    ClearData()

def SelectEmp():
    global index
    ClearData()
    index = listEmp.curselection()[0] #for curser selection at the time of update/give me the first selected item
    # print(index)
    emp = listEmp.get(ACTIVE)
    emp = emp.split(",")
    txEid.insert(0,emp[0])
    txEname.insert(0,emp[1])
    txBasic.insert(0,emp[2])


def deleteEmp():
    listEmp.delete(ACTIVE)


def UpdateEmp():
    eid = txEid.get()
    ename = txEname.get()
    basic = txBasic.get()
    emp = eid+","+ename+","+basic
    listEmp.delete(index)  #del prev element after updated that element
    listEmp.insert(index,emp)
    ClearData()


if __name__ == '__main__':
   
    window = Tk()
    window.title("My Window")
    window.geometry("300x300")
    
    frame1 = Frame(window)
    frame2 = Frame(window)
    frame3 = Frame(window)
    
    frame1.pack()
    frame2.pack()
    frame3.pack()

    LabelEid = Label(frame1,text="Eid")
    LabelEname = Label(frame1,text="Ename")
    LabelBasic = Label(frame1,text="Basic")

    txEid = Entry(frame1)
    txEname = Entry(frame1)
    txBasic = Entry(frame1)

    LabelEid.grid(row=1,column=1)
    LabelEname.grid(row=2,column=1)
    LabelBasic.grid(row=3,column=1)

    txEid.grid(row=1,column=2)
    txEname.grid(row=2,column=2)
    txBasic.grid(row=3,column=2)

    btnAdd = Button(frame2,text="Add",command=addEmp)
    btnSelect = Button(frame2,text="Select",command=SelectEmp)
    btnDelete = Button(frame2,text="Delete",command=deleteEmp)
    btnUpdate = Button(frame2,text="Update",command=UpdateEmp)

    btnAdd.pack(side=LEFT)
    btnSelect.pack(side=LEFT)
    btnDelete.pack(side=LEFT)
    btnUpdate.pack(side=LEFT)

    listEmp = Listbox(frame3)
    listEmp.pack() 
    
    

    window.mainloop()    