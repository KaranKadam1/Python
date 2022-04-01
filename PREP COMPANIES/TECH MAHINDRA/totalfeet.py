'''
Find Total Feet

Given an array of integers representing measurements in inches, write a program to calculate the total 
of measurements in feet. Ignore the measurements that are less than a feet (eg. 10).

Note:
You are expected to write code in the findTotalFeet function only which will receive the first parameter 
as the number of items in the array and second parameter as the array itself. You are not required to take 
input from the console

Example:
Finding the total measurements in feet from a list of 5 numbers

Input
5
18 11 27 12 14

Output
5

Explanation: 12=1feet
The first parameter (5) is the size of the array. Next is an array of measurements in inches. The total 
number of feet is 5 which is calculated as shown below:
18-> 1
11-> 0
27-> 2
12-> 1
14-> 1
'''
def findTotalFeet(num):

    total_feet = 0

    for x in num:
        feet = x//12

        if feet:
            total_feet += feet
    print(total_feet)

n = int(input())
num = list(map(int,input().split()))
findTotalFeet(num)