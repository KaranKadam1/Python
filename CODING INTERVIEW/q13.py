# add two integers without using arithmetic operator

def add(x,y):
    if y==0:
        return x
    else:
        return add(x^y,(x&y)<<1)

x = int(input())
y = int(input())
print(add(x,y))



