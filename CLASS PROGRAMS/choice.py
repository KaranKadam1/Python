print('''1.Add two numbers
2.Even odd
3.Greater of two numbers
4.Area of circle
5.Exit
''')

choice=int(input("enter choice= "))

if choice == 1:
    num1 = int(input("enter num1= "))
    num2 = int(input("enter num2= "))
    print("Addition= ",num1+num2)

elif choice == 2:
    num = int(input("enter num1= "))
    if(num%2 == 0):
        print(num,"is even")
    else:
        print(num,"is odd")

elif choice == 3:
    num1 = int(input("enter num1= "))
    num2 = int(input("enter num2= "))
    if(num1 > num2):
        print(num1,"is grater than",num2)
    else:
        print(num2,"is greater than",num1)

elif choice == 4:
    radius = int(input("Enter the radiud= "))
    area = 3.14* radius*radius
    print("Area of circle= ",area)

elif choice == 5:
    print("End of program")
else:
    print("Invalid choice")

