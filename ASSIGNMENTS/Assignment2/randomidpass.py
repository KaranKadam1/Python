import string
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

#for generating random numbers
random_nums=string.digits
random_len=4
s=[]
s.extend(list(random_nums))  
print("Random num is= ")
number=("".join(random.sample(s,random_len)))
print(number)

# check user entered correct number or not
user=input("enter above number correctly= ")

if(user==number):
    print("you are ready to login....")
else:
    print("you entered false number!")




 