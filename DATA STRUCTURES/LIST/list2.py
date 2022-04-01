# program content all list methods

data = []
choice = 0

while(choice != 10):
    print('''\t\t1.Add an element at the end of list
    \t\t2.Add an element at a specific position in the list
    \t\t3.Display all elements
    \t\t4.Add a new list to existing list
    \t\t5.Remove the last element
    \t\t6.Remove specific element
    \t\t7.Remove element from specific position
    \t\t10.Exit''')
    
    choice = int(input("Enter your choice="))

    if(choice == 1):
        ele = int(input("Enter element from user="))
        #append method is to add element at end of list
        data.append(ele)
        print(data)
    elif(choice == 2):
        ele = int(input("Enter element from user="))
        pos = int(input("Enter the position="))
        #pos represents index 
        data.insert(pos,ele)
        print(data)
    elif(choice == 3):
        print(data)
    elif(choice == 4):
        t = [1,2,3]
        data.extend(t)
        print(data)
    elif(choice == 5):
        x = data.pop()
        print(x)
        print(data)
    elif(choice == 6):
        ele = int(input("Enter element from user which you want to delete="))
        data.remove(ele)
        print(data)
    elif(choice == 7):
        pos = int(input("Enter the position from which you want to remove element="))
        data.pop(pos)
        print(data)
        
