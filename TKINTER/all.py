from tkinter import *

if __name__ == '__main__':

    myWindow = Tk()
    myWindow.title("My Tkinter Window")
    myWindow.geometry("400x400")
    
    Label1 = Label(myWindow,text="First Lable")
    Label2 = Label(myWindow,text="Second Lable")
    Label3 = Label(myWindow,text="Third Lable")
    Label4 = Label(myWindow,text="Fourth Lable")

    # Frame concept
    Label1.pack(side=LEFT)
    Label2.pack(side=RIGHT)
    Label3.pack(side=TOP)
    Label4.pack(side=BOTTOM)

    myWindow.mainloop()