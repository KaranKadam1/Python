
# for i in range(5):
#     age = int(input("enter age of the passanger= "))
#     amount = 2000

#     if(age < 12):
#         pay = amount*0.3
#         print("please pay= ",pay) 

#     elif(age > 59):
#         pay = amount*0.5
#         print("please pay= ",pay)

#     else:
#         print("please pay= ",amount)
  

amount = int(input("enter ticket price= "))
n = int(input("enter the no. of people travelling= "))

total = 0

for i in range(1,n+1):
    age = int(input("enter age of the passanger= "))
    if(age >= 60):
        total += amount-amount*0.5
    elif(age <= 12):
        total += amount-amount*0.3
    else:
        total += amount

print("total ticket price= ",total)



