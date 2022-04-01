
num=int(input("enter no= "))

sum=0

temp=num

while temp>0:
    digit=temp%10
    sum += digit**3
    temp//=10

if num==sum:
    print(num,"is a armtrong number")
else:
    print(num,"is not armstrong number")




def checkarm(num,t,no_of_dig):
    if(num == 0):
        return t
    else:
        d = num%10
        t += d**no_of_dig
        num = num//10
        return checkarm(num,t,no_of_dig)

num = int(input())
no_of_dig = 0
while(num != 0):
    no_of_dig +=1
    num = num//10
num = temp
result = checkarm(num,0,no_of_dig)
if(result == temp):
    print("armstrong")
else:
    print("not")
