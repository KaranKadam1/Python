# Infosys infytq -Identify pallindrome

'''
for a given positive number num,identify the pallindrome formed by performing the following operations-

add num and its reverse and repeat the orocess untill pallindrome is obtained.

exmpl:if original int is 195,we get 9339 as the resulting pallindrome after the fourth addition:
195+591=786+687=1473+3747=5214+4125=9339

sample input-124
output-545

the sum of 124 and its reverse is 421 is 545 which is a palindrome

'''
num = int(input("enter num="))

temp = num
rev = 0
while(num>=1):
    rev = rev*10 + num%10
    num = num//10
sum = temp+rev
print("reverse=",rev)
print("sum=",sum)

temp2 = sum
rev2 = 0
while(sum>=1):
    rev2 = rev2*10+ sum%10
    sum = sum//10
    if(temp2 == rev2):
        print("sum is pallindrome=",rev2)
        break
else:
    print("sum is not pallindrome")



