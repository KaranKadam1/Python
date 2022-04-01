# Reverse an array

def revarr(arr):
    return arr[::-1]

arr = [1,2,3,4,5]
rev = revarr(arr)
print(rev)




def revarr(arr,start,end):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1

arr = [1,2,3,4,5]
revarr(arr,0,4)
print(arr)
