# accept the string from user and count the frequency of each charachter in string

string = input("Enter a string=")
char_set = set(string)

for x in char_set:
    n=string.count(x)
    print(x,"is present",n,"times")