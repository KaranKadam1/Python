# Sample Input 0=
# HackerRank.com presents "Pythonist 2".
# Sample Output 0=
# hACKERrANK.COM PRESENTS "pYTHONIST 2".

def swapcase(s):
    char=" "
    for i in s:
        if i.isupper()==True:
            char+=i.lower()
        elif i.islower()==True:
            char+=i.upper()
        elif i.isspace()==True:
            char+=" "
        elif i.isdigit()==True:
            char+= str(int(i))
        else:
            char+=1
    return char

s=input("enter= ")
s=swapcase(s)
print(s)