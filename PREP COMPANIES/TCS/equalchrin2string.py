# write a program to find whether given two strings contain equal set of characters or not.
'''
EXAMPLE 1
inp-
elbow-val of 1st string
below-val of 2nd string

out-
1    after rearranging elbow becomes below therefore ans is 1

EXAMPLE 2
inp-
nice-val of 1st string
china-value of second string

out-
0
'''
str1 = input()
str2 = input()

if sorted(str1) == sorted(str2):
    print(1)
else:
    print(0)





