from tkinter import *
from tkinter import messagebox


def selectCourse():
    x = var1.get()
    y = var2.get()
    z = var3.get()

    data =""
    if(x==1):
        data = "python diploma"
    if(y==1):
        data += " java diploma"
    if(z==1):
        data += " fullstack diploma"
    if len(data)==0:
        data = "please select any course"
    messagebox.showinfo("Course",data)


if __name__ == '__main__':
   
    window = Tk()
    window.title("My Window")
    window.geometry("300x300")
    
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()

    check1 = Checkbutton(window,text="python diploma",variable=var1)
    check2 = Checkbutton(window,text="java diploma",variable=var2)
    check3 = Checkbutton(window,text="fullstack diploma",variable=var3)
    
    check1.grid(row=1,column=1)
    check2.grid(row=2,column=1)
    check3.grid(row=3,column=1)

    btnselect = Button(window,text="select course",command=selectCourse)

    btnselect.grid(row=4,column=1)
    window.mainloop()