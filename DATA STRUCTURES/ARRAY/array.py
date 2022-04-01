import array

a1 = array.array('i',[1,2,3,4])
print(a1)

for x in a1:
    print(x)

print("length=",len(a1))

# Array is a collection of homogeneous element
# i.e data types must be same

a1.insert(0,11)
print(a1)

a1.append(50)
print(a1)

print(a1.pop())
print(a1.pop(0))

print(a1.index(4))

