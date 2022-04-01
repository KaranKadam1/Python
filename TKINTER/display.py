from tkinter import *
# event = when we click on button is called as event

def displayName():
    # to get the text from Textbox
    name = txtName.get()
    # print("Button is Clicked!!")
    print("Hello",name,"!!!")



if __name__ == '__main__':

    myWindow = Tk()
    myWindow.title("My Tkinter Window")
    myWindow.geometry("250x100")

    Label1 = Label(myWindow,text="Enter your name=")
    # text box
    txtName = Entry(myWindow)
    # button
    btnDisplay = Button(myWindow,text = "Display Name",command=displayName)

    Label1.grid(row=1,column=1)
    txtName.grid(row=1,column=2)
    btnDisplay.grid(row=2,column=1)

    myWindow.mainloop()