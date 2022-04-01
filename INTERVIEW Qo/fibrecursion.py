
def fib(a,b,n):
    if(n == 0):
        return
    else:
        c = a+b
        print(c,end=" ")
        fib(b,c,n-1)

n = int(input("enter num of terms= "))
fib(1,0,n)
# a=1,b=0