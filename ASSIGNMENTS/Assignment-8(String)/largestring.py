# take two strings and display the larger string without using built-in-function

string1 = input("Enter string1=")
string2 = input("Enter string2=")

string1_count = 0
string2_count = 0

for x in string1:
    string1_count += 1

for x in string2:
    string2_count += 1

if(string1_count > string2_count):
    print("Larger string=",string1)
elif(string1_count == string2_count):
    print("Both strings are equal")
else:
    print("Larger string=",string2)
