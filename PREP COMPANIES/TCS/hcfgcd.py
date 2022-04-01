# find HCF/GCD of two numbers
# highest common factor /greatest common divisor

# eg.9,18 =cf-3,9  so hcf is 9

# 14:2*7
# 30:2*3*5 so hcf is 2

# 28=2*7*2
# 12=2*3*2  hcf=2*2=4

def GCD(n1,n2):
    if n2 ==0:
        return n1
    else:
        return GCD(n2,n1%n2)

n1 = int(input("enter first number= "))
n2 = int(input("enter second number= "))
hcf=GCD(n1,n2)
print("hcf=",hcf)
