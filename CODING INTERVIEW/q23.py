# in array 1-100 multiple numbers are duplicates how do you find it?

arr = list(map(int,input().split()))
n = len(arr)

for i in range(0,n):
    for j in range(i+1,n):
        if arr[i] == arr[j]:
            print(arr[j],end=" ")

