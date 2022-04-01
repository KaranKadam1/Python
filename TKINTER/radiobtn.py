from tkinter import *
from tkinter import messagebox


def selectCourse():
    x = var1.get()
    if(x==1):
        data = "you selected python diploma"
    elif(x==2):
        data = "you selected java diploma"
    elif(x==3):
        data = "you selected fullstack diploma"
    else:
        data = "please select any course"
    messagebox.showinfo("Course",data)


if __name__ == '__main__':
   
    window = Tk()
    window.title("My Window")
    window.geometry("300x300")
    
    var1 = IntVar()

    radio1 = Radiobutton(window,text="Python diploma",variable=var1,value=1)
    radio2 = Radiobutton(window,text="java diploma",variable=var1,value=2)
    radio3 = Radiobutton(window,text="FullStack diploma",variable=var1,value=3)
    
    btnselect = Button(window,text="select course",command=selectCourse)
    
    radio1.grid(row=1,column=1)
    radio2.grid(row=2,column=1)
    radio3.grid(row=3,column=1)

    btnselect.grid(row=4,column=1)
    window.mainloop()