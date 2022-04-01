# print odd after even
# input= 8
#        10 98 3 33 12 22 21 11
# output = 10 98 12 22 3 33 21 31

x = int(input())
list = list(map(int,input().split()))
n = len(list)

def evenbefodd(list,n):
    j = 0    #counter
    for i in range(0,n):
        if(list[i]%2 == 0):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
            j += 1  #check next element
    return list

result = evenbefodd(list,n)
for x in result:
    print(x,end=" ")