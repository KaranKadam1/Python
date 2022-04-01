'''
0 
1 0 
0 1 0
1 0 1 0
0 1 0 1 0

'''
for i in range(1,6):
    for j in range(1,i+1):
        if((i+j)%2==0):
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()

'''
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

'''
for i in range(1,6):
    for j in range(1,i+1):
        if((i+j)%2==0):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()


'''
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''

n = int(input())
count = 1
for i in range(1,n):
    for j in range(1,i+1):
        print(count,end=" ")
        count+=1
    print()