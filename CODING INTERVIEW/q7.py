# swap two numbers using third variable 

a =int(input())
b = int(input())
print("before swap=",a,b)

temp = a
a = b
b = temp

print("after swap=",a,b)



# without third variable

a = int(input())
b = int(input())

a,b = b,a
print(a,b)