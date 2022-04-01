'''
Find the 15th term of the series?

0,0,7,6,14,12,21,18, 28

Explanation : In this series the odd term is increment of 7 {0, 7, 14, 21, 28, 35 – – – – – – }

                        And even term is a increment of 6 {0, 6, 12, 18, 24, 30 – – – – – – }
'''

n = int(input("enter a number= "))

odd = 0
even = 0

for i in range(1,n+1):
    if(i%2 != 0):
        odd = odd+7
    else:
        even = even+6

if(n%2 != 0):
    print(f"{n} term of series is : {odd-7}")
else:
    print(f"{n} term of series is : {even-6}")