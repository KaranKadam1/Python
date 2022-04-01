# write a function to print following fibonacci series using function:
# 1 1 2 3 5 8 nterm

def fib(n):
    
    a,b = 1,0
    for i in range(1,n+1):
        c = a + b
        print(c,end=" ")
        a = b
        b = c
    
n = int(input("enter num= "))
fib(n)