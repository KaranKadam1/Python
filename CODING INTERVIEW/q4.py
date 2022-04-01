# fibonacci series with iterative method

def fib(a,b,n):
    for i in range(1,n+1):
        c = a + b
        print(c,end=" ")
        a = b
        b = c
n = int(input())
fib(1,0,n)




n = int(input())
a,b = 1,0
for i in range(1,n+1):
    c = a+b
    print(c,end=" ")
    a = b
    b = c


# with Recursion

def fib(a,b,n):
    if n == 0:
        return
    else:
        c = a+b
        print(c,end=" ")
        fib(b,c,n-1)
    
n = int(input())
fib(1,0,n)