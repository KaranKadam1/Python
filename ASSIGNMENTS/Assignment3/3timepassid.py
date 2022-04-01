print("enter correct username and password to continue!")
num = 0

while(num < 3):
    username = input("enter user-name= ")
    password = input("enter password= ")

    if(username == "123" and password == "karan"):
        print("access granted!")
        break
    else:
        print("access denied!")
        num +=1