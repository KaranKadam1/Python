from mainAdmin import admin

if __name__ == '__main__':
    print("\t1.Admin Menu")
    print("\t2.User Menu")

    choice = int(input("enter your choice="))
    if choice == 1:
        username = input("enter username=")
        password = input("enter password=")
        if(username == "Admin" and password == "FirstBit"):
            admin()
        else:
            print("invalid credential..")
    elif(choice==2):
        # user()
        print("User Menu")
    