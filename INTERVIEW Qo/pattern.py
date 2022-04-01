
k=7

for i in range(1,6):
    ch=65
    for j in range(1,i+1):
        print(chr(ch),end=" ")
        ch+=1
    
    for k in range(1,k+1):
        print(" ",end=" ")
    k-=2

    ch-=1

    for j in range(1,i+1):
        if(j==1 and i==5):
            print("",end="")
        else:
            print(chr(ch),end=" ")
        ch-=1
    print()


    '''
A               A 
A B           B A 
A B C       C B A
A B C D   D C B A
A B C D E D C B A
   
    
    '''