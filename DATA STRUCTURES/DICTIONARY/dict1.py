# dictionary is unordered collection of key value pair.where keys are unique where seq is not important
# value may be duplicate


# creating an dictionary
data = {101:"Atul",104:"Rashmi",106:"Seema",110:"Tejas",101:"Shruti"}
print(data)
print(data[110]) #gives value of key 110

for x in data:
    print(x)  #print all keys


# it will fetch the keys
print(data.keys())

# it will fetch the values
print(data.values())

# it will fetch the items,it represents key value pair
print(data.items())


print("------------keys-------------")
for key in data.keys():
    print(key)

print("------------values-------------")
for value in data.values():
    print(value)

print("------------items-------------")
for key,value in data.items():
    print(key,"=",value)


# for updating data
x = {1:"AAAA",2:"BBBB",3:"CCCC"} #new dictionary
data.update(x) #it will add new dictionary to existing dictionary
print(data)







