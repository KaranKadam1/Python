# write a program to print first n prime numbers

num = int(input("enter num= "))

for n in range(1,num):
    for i in range(2,n):
        if(n%i == 0):
            break

    else:
        print(n,end=" ")