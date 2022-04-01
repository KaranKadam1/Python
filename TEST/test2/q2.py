# 2.	Write a program to calculate the sum of following series where n is input by user. 
# 1/1! + 2/2! + 3/3! + 4/4! + ... N/N!


# def sumOfSeries(num):
#     res = 0
#     fact = 1
#     for i in range(1, num+1):
#        fact *= i
#        res = res + (i/ fact)
#     return res
# n = int(input("enter num= "))
# print("Sum: ", sumOfSeries(n))

n = int(input("enter num= "))

sum = 0
fact = 1
for i in range(1,n+1):
    fact= fact*i
    sum += (i/fact)
print("sum of series= ",sum)

