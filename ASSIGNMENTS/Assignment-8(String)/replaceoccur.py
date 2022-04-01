# Replace all occurence of 'a' with $ in a string

string1 = input("enter string=")
 
if 'a' in string1:
    string=string1.replace('a','$')
print("Original string=",string1)
print("Modified String=",string)
