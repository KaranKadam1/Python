#contiguous sub-array with maximum sum
# kadanes algorithm

def maxsubarr(arr,n):
    max_till_now = arr[0]
    max_ending = 0

    for i in range(0,n):
        max_ending = max_ending + arr[i]
        if(max_ending < 0):
            max_ending = 0
        elif(max_till_now < max_ending):
            max_till_now = max_ending
    return max_till_now

arr = [1,2,3,-2,5]
n = len(arr)

arr = maxsubarr(arr,n)
print("sub-array with maximum sum= ",arr)





