
num=int(input("enter num= "))
temp=num
rev=0
while(num>0):
    rev=rev*10 + num%10
    num=num//10

if(temp==rev):
    print("num is palindrom")
else:
    print("num is not palindrom")