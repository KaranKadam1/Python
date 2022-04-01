'''
write a program to find sum of following series using function
1! +  2! + 3! + 4! + ….+n! 
'''
def sum(n):
    sum = 0
    for i in range(1,n+1):
        f=1
        for j in range(1,i+1):
            f = f*j
        sum += f
    print("sum=",sum)
    print("factorial=",f)

n = int(input("enter num="))
sum(n)


