# num=int(input("enter three dig num="))
# w=num//10
# x=w//10
# y=w%10
# z=num%10

# sum=x+y+z
# print("sum of digits= ",sum)

num=int(input("enter three dig num="))
sum=0

sum+=num%10
num //=10

sum+=num%10
num //=10

sum+=num%10
num //=10

print("sum of digits= ",sum)
