
number=int(input("enter no= "))
reverse=0
while(number>0):
   reverse=(reverse*10)+(number%10)
   number=number//10

print("reverse no of",number,"is=",reverse)