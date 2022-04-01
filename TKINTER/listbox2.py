from tkinter import *
from tkinter import messagebox


def addtolist1():
    item = List2.get(ACTIVE)
    List1.insert(END,item)
    List2.delete(ACTIVE)
    
def addtolist2():
    item = List1.get(ACTIVE)
    List2.insert(END,item)
    List1.delete(ACTIVE)


if __name__ == '__main__':
   
    window = Tk()
    window.title("My Window")
    window.geometry("300x300")
    
    List1 = Listbox(window)
    List1.insert(END,"first")
    List1.insert(END,"second")
    List1.insert(END,"third")
    List1.insert(END,"fourth")
    

    List2 = Listbox(window)
    List2.insert(END,"one")
    List2.insert(END,"two")
    List2.insert(END,"three")
    List2.insert(END,"four")

    btnAdd1 = Button(window,text=">>",command=addtolist2)
    btnAdd2 = Button(window,text="<<",command=addtolist1)

    List1.grid(row=1,column=1)
    btnAdd1.grid(row=1,column=2)
    btnAdd2.grid(row=1,column=3)
    List2.grid(row=1,column=4)

    window.mainloop()