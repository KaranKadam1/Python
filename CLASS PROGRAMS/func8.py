
def fact(n):
    f=1
    while(n>=1):
        f=f*n
        n-=1
    return f

n = int(input("Enter num= "))
fact = fact(n)
print("Factorial of given number is= ",fact)