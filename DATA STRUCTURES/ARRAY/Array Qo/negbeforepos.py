# move all negative element before positive

arr = [1,-2,4,8,-3,7]
n = len(arr)

def negbeforepos(arr,n):
    j = 0
    for i in range(0,n):
        if(arr[i]<0):
           temp = arr[i]
           arr[i] = arr[j]
           arr[j] = temp
           j+=1
    return arr

arrange = negbeforepos(arr,n)
print("Negative element before positive=",arrange)