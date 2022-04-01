'''
Return the difference between the largest and smallest numbers from an array of positive integers.

input =  5
input2 = 10 11 7 12 14

output = 7
'''

def findDiff(arr):
    n = len(arr)

    max = arr[0]
    min = arr[0]

    for i in range(1,n):
        if(max < arr[i]):
            max = arr[i]
        elif(min > arr[i]):
            min = arr[i]
    print(max-min)

n = int(input())
arr = list(map(int,input().split()))
findDiff(arr)