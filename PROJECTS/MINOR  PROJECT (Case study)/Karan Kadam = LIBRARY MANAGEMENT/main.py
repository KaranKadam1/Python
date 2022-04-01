from mainAdmin import admin
from mainUser import user
import random


if(__name__ == "__main__"):
    print("\n<<<<--Choose Login Option To Proceed-->>>>")
    print("\n\t1.ADMIN MENU")
    print("\t2.USER MENU\n")

    choice = int(input("Enter your choice = "))
    if(choice == 1):
        print("\n<<------------------ADMIN MENU--------------------->>\n")
        username = input("Enter username = ")
        password = input("Enter password = ")
        if(username == "Admin" and password == "Admin"):
            print("\nlogin succesfully!!")
            print("\n")
            admin()
        else:
            print("\nInvalid credentials...")

    elif(choice == 2):
        print("\n<<<------------------USER MENU------------------>>\n")
        username = input("Enter username = ")
        password = input("Enter password = ")
        Captch = random.randint(1000,9000)
        print("Captcha = ",Captch)
        cp = int(input("Enter above captcha to proceed = "))
        if(username == "Karan" and password == "12345" and cp == Captch):
            print("\nlogin succesfully!!")
            print("\n")
            user()
        else:
            print("\nInvalid credentials..")
        
        
        
    
