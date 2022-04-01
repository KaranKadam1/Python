# find prime factors of a given integer

num = int(input())

for n in range(1,num):
    for i in range(2,n):
        if(n%i == 0):
            break
    else:
        print(n,end=" ")