# kth largest using bubble sort

arr = [40,10,30,70,45]

n = len(arr)

for j in range(1,n):
    for i in range(n-j):
        if(arr[i] > arr[i+1]):
            arr[i],arr[i+1] = arr[i+1],arr[i]

print(arr)
k = int(input("enter k value= "))
print("smallest= ",arr[k-1])
print("largest= ",arr[n-k])
        

