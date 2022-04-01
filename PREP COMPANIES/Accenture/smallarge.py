'''
def LargeSmallSum(arr)

The function accepts an integers arr of size ’length’ as its arguments you are required to return
the sum of second largest largest element from the even positions and second smallest from the odd
position of given ‘arr’

Assumption:
All array elements are unique
Treat the 0th position a seven

NOTE
Return 0 if array is empty
Return 0, if array length is 3 or less than 3

Example
Input-
arr:3 2 1 7 5 4
Output-
7

Explanation=
    Second largest among even position elements(1 3 5) is 3
    Second largest among odd position element is 4
    Thus output is 3+4 = 7

Sample Input=
arr:1 8 0 2 3 5 6
Sample Output
8
'''


arr = list(map(int,input().split()))
n = len(arr)

even = []
odd = []

for i in range(n):
    if i%2 == 0:
        even.append(arr[i])
    else:
        odd.append(arr[i])

even = sorted(even)
odd = sorted(odd)

sec_large_even = even[len(even)-2]
sec_large_odd = odd[len(odd)-2]

sum = sec_large_even + sec_large_odd
print(sum)
