# check if given key is existing in a dictionary or not

dict = {1:40,2:50,3:65,4:80}

key = int(input("enter key to check="))

if(key in dict.keys()):
    print(key,"key is present")
else:
    print(key,"key is not present")
