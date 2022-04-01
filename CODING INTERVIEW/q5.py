# Palindrome number using iterative method

num = int(input())
temp = num
rev = 0
while(num>0):
    rev = rev*10 + num%10
    num //= 10
if(temp == rev):
    print("Palindrome")
else:
    print("Not Palindrome")


# recursive mode

def palindrome(n,rev):
    if n == 0:
        return rev
    rev = rev*10 + n%10
    return palindrome(int(n/10),rev)

n = int(input())
rev = 0
p = palindrome(n,rev)

if(p == n):
    print("Palindrome")
else:
    print("Not Palindrome")