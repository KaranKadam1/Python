num1 = int(input("Enter num 1= "))
num2 = int(input("Enter num 2= "))

print("operators= (+,-,/,*,**)")
op = input("enter operator= ")

if(op == "+"):
    result = num1 + num2
elif(op == "-"):
    result = num1 - num2
elif(op == "/"):
    result = num1 / num2
elif(op == "*"):
    result = num1*num2
elif(op == "**"):
    result = num1**num2
else:
    print("invalid !")

print("Result= ",result)