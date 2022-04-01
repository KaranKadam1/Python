# tuple is also ordered collection and it is imutable and faster than list

t1 = (10,20,30,40)
print(t1)

for x in t1:
    print(x)

# error->

# t1[0] = 22
# del t1[0]

t1 = 10,20,30,40  #another technique to write tuple
print(t1)

t1 = (10,) #tuple of one element

t1 = 10,20,30,40
print(t1[0:3])
print(t1[-1])


t1 = (10,20,30,[1,2,3])
print(t1[3][1])

t1[3][1]=22
print(t1)

t1 = (23,1,45,22,56,78,10,99,4)
print("Maximum element ",max(t1))
print("minimum element ",min(t1))
print(t1.count(23))
myList =list(t1)
print(sum(t1))
print(myList) 
t2 = tuple(myList)
print(t2)

myList.sort()
print(myList)

myList.reverse()
print(myList)

