ans=input("Are you a male(y/n)")
age=int(input("Enter your age"))

if(ans == "y" or ans == "Y"):
    if(age>=21):
        print("you are eligible to marry")
    else:
        print("you are not eligible to marry")

else:
    if(age>=18):
        print("you are eligible to marry")
    else:
        print("you are not eligible to marry")