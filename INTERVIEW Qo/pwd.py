pwd = input("enter your pass=")

verify = False
digit = False
caps = False
special = False

for x in pwd:
    if x.isdigit():
        digit = True
    if(ord(x) >= 65 and ord(x)<92):
        caps = True
    if x == "/" or x == " ":
        special = True
    
if (len(pwd) >=4 and digit and caps and not special and not pwd[0].isdigit()):
    print("password is valid")
else:
    print("password is invalid")
    

