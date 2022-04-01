# sort according to 1 2 3

def sort123(list,n):
    i = 0
    j = 0
    k = n-1

    while j<=k:
        if(list[j] == 1):
            list[i],list[j] = list[j],list[i]
            i += 1
            j += 1

        elif(list[j] == 2):
            j += 1

        elif(list[j] == 3):
            list[j],list[k] = list[k],list[j]
            k -= 1
    return list

list = list(map(int,input().split()))
n = len(list)
result = sort123(list,n)
for x in result:
    print(x,end=" ")