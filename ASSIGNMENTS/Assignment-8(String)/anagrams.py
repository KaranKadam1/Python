# Check if two strings are anagrams with inbuilt function
'''
inp s1 = "listen"
    s2 = "silent"
out = anagrams
'''
s1 = input("enter string 1 =")
s2 = input("enter string 2 =")

if(sorted(s1) == sorted(s2)):
    print("The strings are anagrams")
else:
    print("The strings aren't anagrams")





# without using inbuilt function

def getlist(string):
    return [ch for ch in string]

def sortstring(string):
    for i in range(len(string)-1):
        for j in range(len(string)-i-1):
            if(string[j]>string[j+1]):
                string[j],string[j+1] = string[j+1],str[j]
    return string

first = input("enter first string=")
second = input("enter second string=")

first = getlist(first)
second = getlist(second)
first = sortstring(first)
second = sortstring(second)
# print(first,second)
# convert string to list

first = "".join(first)
second = "".join(second)

if(first == second):
    print("anagram")
else:
    print("not anagram")


