# count frequency of words appearing in a string using dictionary

string = input("Enter string=")
x =[]
x = string.split()

mydict={}
for key in x:
    mydict[key]=x.count(key)
print(mydict)