# find lowest common multiple of two numbers

# eg.24 ->24,48,72,96....
# 36 -> 36,72,108,144....
# lcm of 24 and 36 is 72

def LCM(n1,n2):
    if(n1>n2):
        higher = n1
    else:
        higher = n2
    temp = higher

    while True:
        if(higher%n1 == 0 and higher%n2 == 0):
            print(f"LCM of {n1} and {n2} is {higher}")
            break
        else:
            higher=higher+temp


n1 = int(input("enter first number= "))
n2 = int(input("enter second number= "))
LCM(n1,n2)


