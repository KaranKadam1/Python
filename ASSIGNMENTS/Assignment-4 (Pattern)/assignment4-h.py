
k=7

for i in range(1,6):
    ch=1
    for j in range(1,i+1):
        print(ch,end="")
        ch+=1

    for k in range(1,k+1):
        print(" ",end="")
    k-=2

    ch-=1
    for j in range(1,i+1):
        if(j==1 and i==5):
            print("",end="")
        else:
            print(ch,end="")
        ch-=1
    print()
print()


'''
1       1
12     21
123   321
1234 4321
123454321

'''