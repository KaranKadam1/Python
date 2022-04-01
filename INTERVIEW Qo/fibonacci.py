n = int(input("Enter num= "))

a,b = 1,0

for i in range(1,n+1):
    c = a+b
    print(c,end=" ")
    a = b
    b = c

# with function
n = int(input())
def fib(a,b,n):
    a,b = 1,0
    
    for i in range(1,n+1):
        c = a+b
        print(c,end=" ")
        a = b
        b = c
    return c
print(fib(0,1,n))