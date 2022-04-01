# write a program to create a duplicate of an existing list.it should not point the same list

l1 = [1,2,3,4,5]
l2 = []

for x in l1:
    l2.append(x)
print("original list=",l1)
print("duplicate list=",l2)