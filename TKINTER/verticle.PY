# developing gui based aplication in python

# import tkinter 
from tkinter import *

if __name__ == '__main__':
    # it will create tkinter window
    # myWindow = tkinter.Tk()
    myWindow = Tk()
    myWindow.title("My Tkinter Window")
    myWindow.geometry("400x400")
    
    Label1 = Label(myWindow,text="First Lable")
    Label2 = Label(myWindow,text="Second Lable")
    Label3 = Label(myWindow,text="Third Lable")
    Label4 = Label(myWindow,text="Fourth Lable")

    # Frame concept
    Label1.pack()
    Label2.pack()
    Label3.pack()
    Label4.pack()


    myWindow.mainloop()


    