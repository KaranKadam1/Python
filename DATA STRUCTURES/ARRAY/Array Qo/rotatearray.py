# Cyclically rotate an array by one 
'''
Given an array, rotate the array by one position in clock-wise direction.
 
Example 1:
Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
5 1 2 3 4

Example 2:
Input:
N = 8
A[] = {9, 8, 7, 6, 4, 2, 1, 3}
Output:
3 9 8 7 6 4 2 1
'''

# Using List-Slicing

N = int(input())
A = list(map(int,input().split()))

def rotate(A):
    return ([A[-1]] + A[0:-1])

x = rotate(A)
for i in x:
    print(i,end=" ")

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Approach-2

def rotate(arr, n):
    x = arr[n-1]

    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = x

N = int(input())
arr = list(map(int,input().split()))
n = len(arr)
rotate(arr,n)

for i in range(0,n):
    print(arr[i],end =" ")
