# sum of digits

def sum_of_digit(n):
    if(n==0):
        return 0
    else:     #last dig=n%10
        return n%10 + sum_of_digit(n//10)

num = int(input("enter num= "))
result = sum_of_digit(num)
print(result)
