data = {101:"Atul",104:"Rashmi",106:"Seema",110:"Tejas",101:"Shruti"}

choice = 0

while(choice != 10):
    print('''\t\t1.Add item
    \t\t2.Remove a random item
    \t\t3.Remove item based on key
    \t\t4.Search for item based on key
    \t\t5.Display
    \t\t6.Edit item
    \t\t10.Exit''')

    choice = int(input("Enter your choice="))

    if(choice == 1):
        key = int(input("enter key="))
        value = input("enter value=")
        data[key] = value
    elif(choice == 2):
        print(data.popitem())  #it will remove random item
    elif(choice == 3):
        key = int(input("enter key=")) #it will remove item with specific key
        data.pop(key)
    elif(choice == 4):
        key = int(input("enter key to search="))
        if(key in data):
            print("Present: ",data[key])
        else:
            print("Not present")
    elif(choice == 5):
        print(data)
    elif(choice == 6):
        key = int(input("enter key whose value you want to modify="))
        if(key in data):
            val = input("enter new value=")
            data[key]=val
        else:
            print(key,"is not present")

