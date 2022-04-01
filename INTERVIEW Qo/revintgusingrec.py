# reverse integer using recursion

def revint(n,r):
    if(n==0):
        return r
    else:
        return revint(n//10, r*10 + n%10)

r=0
n = int(input("enter num="))
rev = revint(n,r)
print(rev)


# rev int without recursion

num = int(input("enter num="))
rev=0
while(num>0):
    rev = rev*10 + num%10
    num = num//10

print("reverse integer= ",rev)