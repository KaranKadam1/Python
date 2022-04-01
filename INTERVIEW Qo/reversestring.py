# reverse a given string

string = input("enter a string to reverse=")

result=" "

for x in string:
    result = x + result
print("reverse string= ",result)