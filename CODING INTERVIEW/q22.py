# in array 1-100 numbers are stored,one is missing how do you find it

def getMissing(arr):
    n = len(arr)
    
    total = (n+1)*(n+2)/2
    arr_sum = sum(arr)

    return total - arr_sum

arr = list(map(int,input().split()))
miss = getMissing(arr)
miss = int(miss)
print(miss)