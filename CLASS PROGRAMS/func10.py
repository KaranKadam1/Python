
def fact(x):
    f=1
    while(x>=1):
        f=f*x
        x-=1
    return f

def sum(x,y):
    return x+y

def greater(x,y):
    if(x>y):
        return x
    else:
        return y

x = int(input("enter x= "))
y = int(input("enter y= "))

z = fact(x)
print("factorial=",z)

z = sum(x,y)
print("sum= ",z)

z = greater(x,y)
print("greater= ",z)