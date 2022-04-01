# Decorators=

def myFun():
    print("I am display function")

x = myFun #myFun represents address of function
x()  #calling myFun




def f1():
    print("I am function 1")
def f2():
    print("I am function 2")

def demo_fun(t,r): #t and r are functions
    def test():
        t()
        print("I am within test")
        r()
    return test
x = demo_fun(f1,f2)
x()

'''
used for step by step exicution and what we have to print first

output=
I am function 1
I am within test
I am function 2
'''





# def demo(t,r): here demo(f1,f2) contents address of f1 anf f2 which pass to t and r
# demo(f1,f2)
# t()
# r()


# def showMenustored():

# def mouse_click_start():
#     show_menu_screen()
# someone else will call the method



# def demo fun(t,r):
#     def test():
#         t()
#         print("my data")
#         r()
#     retun test
# function returning a function


def myDecorator(test):
    def wrapper():
        login()
        test()
        logout()
    return wrapper

@myDecorator
def f1():
    print("I am f1 method")
@myDecorator
def f2():
    print("I am f2 method")
def f3():
    print("i am f3 method")


def login():
    print("I am login method")
def logout():
    print("I am logout method")

f1()
'''
I am login method
I am f1 method
I am logout method
'''
f2()
'''
I am login method
I am f2 method
I am logout method
'''
 

