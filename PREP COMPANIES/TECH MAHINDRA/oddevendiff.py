'''
Odd Even Difference
Write a program to return the difference between the sum of odd and even numbers from an array of positive
integers.

Note:
You are expected to write code in the findOddEvenDifference function only which will receive the first 
parameter as the number of items in the array and second parameter as the array itself. You are not 
required to take input from the console

Example:
Finding the difference between the sum of odd even numbers from a list of 5 numbers

Input
5
10 11 7 12 14

Output
-18

Explanation
Sum of Odd - Sum of Even = 18-36 = -18
'''

def findOddEvenDifference(arr):
    even_sum = 0
    odd_sum = 0
    for x in arr:
        if(x%2 == 0):
            even_sum += x
        else:
            odd_sum += x
    print(odd_sum-even_sum)


arr_len = int(input())
arr = list(map(int,input().split()))
findOddEvenDifference(arr)
