# write a program to check if given number is armstrong or not using recursion

def armstrong(n):
    if n < 10:
        return n*n*n
    return (n%10)*(n%10)*(n%10) + armstrong(int(n/10))

num=int(input("Enter no= "))
r=armstrong(num)

if r==num:
    print(num,"is armstrong number")
else:
    print(num,"is not armstrong number")

