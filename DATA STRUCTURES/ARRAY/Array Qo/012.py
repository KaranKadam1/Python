# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

def sort012(arr,n):

    i = 0
    j = 0
    k = n-1

    while j<=k:
        if(arr[j] == 0):
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j += 1
        elif(arr[j] == 1):
            j += 1
        elif(arr[j] == 2):
            arr[j],arr[k] = arr[k],arr[j]
            k -= 1
    return arr

arr=[0,1,0,0,2,2,1,0,1,2]
n=len(arr)
sort = sort012(arr,n)
print(sort)