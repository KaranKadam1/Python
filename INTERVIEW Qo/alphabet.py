'''
given a string, add+1 to each alphabet only and then after conversation if the final string have any vowels
then convert that vowel into uppercase

eg:hello3!
output=Ifmmp3!
'''
# A->65
# a->97
# 0->48
# ch='a'
# print(chr(ord(x)+1))


# find no of alphabets in given string

string = input("Enter a string=")
count = 0
for x in string:
    if(x.isalpha()):
        count += 1
print("alphabets count=",count)

# add+1 to given string

string = input("Enter a string=")
result = ""

for x in string:
    if(x.isalpha()):
        ch = chr(ord(x)+1)
        if(ch in "aeiou"):
            result += ch.upper()
        else:
            result += ch
    else:
        result += x
print(result)
