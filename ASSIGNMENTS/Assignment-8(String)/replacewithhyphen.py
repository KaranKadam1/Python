# replace every blank space with hyphen in string

string = input("Enter a string=")

for x in string:
    if(x == ' '):
        print(string.replace(' ','-'))