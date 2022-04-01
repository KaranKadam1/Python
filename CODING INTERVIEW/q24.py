# how to find all pairs in array of integers whose sum is equal to given number
# eg input=arr=[1,5,7,-1]  sum=6  output=2


def getpairscount(arr,n,sum):

    count = 0

    for i in range(0,n):
        for j in range(i+1,n):
           if arr[i] + arr[j] == sum:
               count += 1

    return count

arr = list(map(int,input().split()))
n = len(arr)
sum = 6

print("Pairs = ",getpairscount(arr,n,sum))

