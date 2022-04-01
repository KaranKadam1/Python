myset = {10,20,30,40,10,20}
print(myset)

#Add new element
myset.add(60)
print(myset)

# add collection to data/Update set
data = [1,2,3]
myset.update(data)
print(myset)

# add will add single value 
# update will add multiple vals

print(myset.pop()) #remove random elements
print(myset)

myset.remove(10) #remove 10 from set
print(myset)

for x in myset:
    print(x)

