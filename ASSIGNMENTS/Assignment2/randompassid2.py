import random

#for id pass authenticate
User_Id=123
Pass="karan"

id=int(input("enter user id= "))
password=input("enter password= ")

if(id == User_Id and password == Pass):
    print("you are ready to login...")
else:
    print("wrong id or pass !")


# for random num check
captcha = random.randint(1,9999)
print("your captcha is= ",captcha)
check = int(input("Please enter above number= "))

if(check == captcha ):
    print("captcha Granted !")
else:
    print("invalid captcha !")