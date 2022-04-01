# write a program to find sum of following series using functions:
# 1!+2!+3!+4!+...+n!
#note: for fact and sum two recursive function

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


def sum(n):
    if(n==0):
        return 0
    else:
        return fact(n)+sum(n-1)

n = int(input("Enter the value of n="))

factorial = fact(n)
print("Factorial=",factorial)
result = sum(n)
print("sum=",result)