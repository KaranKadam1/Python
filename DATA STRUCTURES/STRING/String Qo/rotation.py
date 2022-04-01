# A Program to check if strings are rotations of each other or not
# Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1? 
# (eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)

def checkRotation(str1,str2):
    temp=""

    if len(str1) != len(str2):
        return False

    temp = str1 +str1

    if str2 in temp:
        return True
    else:
        return False

str1 = input("enter str1=")
str2 = input("enter str2=")

if checkRotation(str1,str2):
    print("Given Strings are rotations of each other.")
else:
    print("Given Strings are not rotations of each other.")
