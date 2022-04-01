
data = [10,10,10,20,20,30,30,30,30]
#Gives the frequency of 10
print(data.count(10))

print(data.count(20))

print(data.count(30))

result = set(data)
for x in result:
    print(x,"=",data.count(x))
