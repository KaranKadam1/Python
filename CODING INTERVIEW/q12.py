# perfect number 6,28 
# a positive int that is equal to the sum of its proper divisors

num = int(input())

sum = 0

for i in range(1,num):
    if(num%i == 0):
        sum = sum + i

if(sum == num):
    print("perfect")
else:
    print("Not Perfect")