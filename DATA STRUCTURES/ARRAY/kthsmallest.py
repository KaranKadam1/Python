def kthsmallest(arr,n,k):
    
    for j in range(1,n):
        for i in range(n-j):
            if(arr[i] > arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]

             
    return arr[k-1]

arr = [3,2,8,4,9,5]
n = len(arr)
k = int(input("enter k= "))

print(kthsmallest(arr,n,k))
