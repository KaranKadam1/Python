# count occurrence of a given character in string
string = input()
char = input()

if char in string:
    print(string.count(char))
   

string = input()
char = input()
count = 0

for i in range(len(string)):
    if string[i] == char:
        count += 1
print(count)
