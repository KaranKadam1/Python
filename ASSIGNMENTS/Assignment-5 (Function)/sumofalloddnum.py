# sum of all odd numbers between 1to n

def sumofodd(n):
    
    sum = 0
    for i in range(0,n+1):
        if(i%2 != 0):
           sum += i
    print("sum of all odd numbers=",sum)


n = int(input("enter num="))
sumofodd(n)