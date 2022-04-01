# remove any given character from strings

string = input()
n = int(input())
first = string[:n]
last = string[n+1:]
new  = first+last
print(new)




string = input()
char = input()
new = string.replace(char,"")
print(new)