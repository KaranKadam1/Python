for i in range(1,6):
    for j in range(1,i+1):
        if(i%2 == 0):
            print("*",end=" ")
        else:
            print(j,end=" ")
    print()

    '''
1 
* * 
1 2 3
* * * *
1 2 3 4 5
 
    '''