# Smallest element in an array that is repeated exactly ‘k’ times.
'''
Input : arr[] = {2 2 1 3 1}
        k = 2
Output: 1
Explanation:
Here in array,
2 is repeated 2 times
1 is repeated 2 times 
3 is repeated 1 time
Hence 2 and 1 both are repeated 'k' times
i.e 2 and min(2, 1) is 1

Input : arr[] = {3 5 3 2}
        k = 1
Output : 2
Explanation:
Both 2 and 5 are repeating 1 time but
min(5, 2) is 2
'''
max = 1000

def smallest(arr,n,k):

    res= max+1

    for i in range(0,n):
        if(arr[i]>0):
            count = 1

            for j in range(i+1,n):
                if(arr[i] == arr[j]):
                   count += 1
        
            if(count == k):
                res = min(res,arr[i])
    return res

arr = [2,2,1,3,1]
n = len(arr)
k = int(input())
print(smallest(arr,n,k))



