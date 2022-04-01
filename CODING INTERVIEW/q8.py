# sum of digits using recursion
def sumofdigits(num):
    if num == 0:
        return 0
    else:
        return num%10 + sumofdigits(num//10)

num = int(input())
result = sumofdigits(num)
print(result)


# without recursion

num = int(input())
sum = 0

while num>0:
    sum += num%10
    num //= 10
print(sum)
