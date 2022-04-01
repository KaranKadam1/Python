# calculate number of words and the number of characters present in string

'''
Enter string= hello world
2 -word
11 - chars
'''

string = input("Enter string= ")

char = 0
word = 1

for x in string:
    char = char+1
    if(x == ' '):
        word = word + 1

print(word)
print(char)

   

