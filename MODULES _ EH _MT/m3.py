x = int(input("enter your age between(20-40)="))

if(x>=20 and x<=40):
    print("your age is:",x)
else:
    # create this situation as an error
    raise IndexError()
    print("Invalid age")

# raise = to explicitly create an error



# nesting of try except block
try:  
    num1 = int(input("enter num1="))  
    num2 = int(input("enter num2="))

    try:
        result = (num1/num2)
    except ZeroDivisionError:
        print("you have entered second number as zero")

except ValueError:
    print("you have entered invalid number")