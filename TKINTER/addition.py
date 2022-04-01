from tkinter import *
from tkinter import messagebox

def addition():
    num1 = int(txNum1.get())
    num2 = int(txNum2.get())
    result = num1 + num2
    # print(result)
    # messagebox.showinfo("result",result)
    txNum3.insert(0,result)      #for showing ans in textbox
    Label3.configure(text=result)   #for showing ans in lable


if __name__ == '__main__':
    window = Tk()
    window.title("My Window")
    window.geometry("300x300")

    Label1 = Label(window,text = "Enter First Number=")
    Label2 = Label(window,text = "Enter Second Number=")
    Label3 = Label(window,text = "")

    txNum1 = Entry(window)
    txNum2 = Entry(window)
    txNum3 = Entry(window)


    btnAdd = Button(window,text="Add",command=addition)


    Label1.grid(row=1,column=1)
    Label2.grid(row=2,column=1)
    txNum1.grid(row=1,column=2)
    txNum2.grid(row=2,column=2)
    txNum3.grid(row=3,column=2)
    btnAdd.grid(row=3,column=1)
    Label3.grid(row=4,column=1)

    window.mainloop()