
def fact(n):
    f=1
    while(n>=1):
        f=f*n
        n-=1
    return f

n = int(input("Enter num= "))
sum=0
for i in range(1,n+1):
    sum = sum + fact(i)
print("sum=",sum)