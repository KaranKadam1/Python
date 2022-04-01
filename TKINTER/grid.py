from tkinter import *

if __name__ == '__main__':

    myWindow = Tk()
    myWindow.title("My Tkinter Window")
    myWindow.geometry("400x400")
    
    Label1 = Label(myWindow,text="First Lable")
    Label2 = Label(myWindow,text="Second Lable")
    Label3 = Label(myWindow,text="Third Lable")
    Label4 = Label(myWindow,text="Fourth Lable")


    # Grid concept
    Label1.grid(row=1,column=1)
    Label2.grid(row=2,column=2)
    Label3.grid(row=3,column=3)
    Label4.grid(row=4,column=4)

    myWindow.mainloop()