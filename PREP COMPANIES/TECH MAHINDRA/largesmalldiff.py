# write a program to return the difference between the largest and smallest numbers from an array of positive 
# integers
# note: you are expected to write code in the findLargeSmall\Difference function only which will recieve the
# first parameter as the number of items in the array and second parameter as the array itself,you are not
# required to take input from the console

# Example=
# finding the difference between the largest and smallest from a list of 5 numbers

# input1:5
# input2:10 11 7 12 14

# output: 7 cause tha diff between largest 14 and smallest 7 is 7





# def findDifference(arr):
#     maximum = max(arr)
#     minimum = min(arr)
    
#     print(maximum-minimum)


# arr_len = int(input())
# arr = list(map(int,input().split()))
# diff = findDifference(arr)






def findDiff(arr):
    n = len(arr)
    max = arr[0]
    min = arr[0]
    
    for i in range(1,n):
        if max < arr[i]:
            max = arr[i]
        elif min > arr[i]:
            min = arr[i]
    print(max - min)

arr = list(map(int,input().split()))
findDiff(arr)
