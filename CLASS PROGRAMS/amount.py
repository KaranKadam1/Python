amount=float(input("enter the amount of purchase= "))

if(amount >= 2000):
    dis=amount*0.3
else:
    dis=amount*0.05

total= amount-dis

print("you got discount of= Rs.",dis)
print("please pay Rs.",total)