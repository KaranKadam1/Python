from invalidageerror import InvalidAgeError

try:
    x = int(input("enter your age between(20-40)="))

    if(x>=20 and x<=40):
        print("your age is:",x)
    else:
        raise InvalidAgeError(x)

except InvalidAgeError as e:
    print(e)   