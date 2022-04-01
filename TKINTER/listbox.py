from tkinter import *
from tkinter import messagebox


def AddToList():
    data = txData.get()
    myList.insert(END,data)
    txData.delete(0,END)   #for clearing inserted data from input

if __name__ == '__main__':
   
    window = Tk()
    window.title("My Window")
    window.geometry("300x300")
    
    txData = Entry(window)
    txData.pack()
    btnAdd = Button(window,text="Add to List",command=AddToList)
    btnAdd.pack()
    myList = Listbox(window)
    myList.insert(END,"first")
    myList.insert(END,"second")
    myList.insert(END,"third")
    myList.insert(END,"fourth")
    myList.pack()


    
    window.mainloop()