# count no.of vowels,consonents,digits,spaces in given string

string = input("Enter a string=")

v = 0
d = 0
s = 0
c = 0

for x in string:
    if(x in "aeiou"):
        v += 1
    elif(x.isdigit()):
        d += 1
    # elif(x in "0123456789")
    elif(x.isspace()):
        s += 1
    else:
        c += 1

print("vowels=",v)
print("digits=",d)
print("spaces=",s)
print("consonent=",c)