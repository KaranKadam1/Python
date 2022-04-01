# write a program to find max and min element in list without using inbuilt function

l1 = [1,2,3,4,5]
n = len(l1)

max = l1[0]
min = l1[0]

for i in range(1,n):
    if max < l1[i]:
        max = l1[i]
    elif min > l1[i]:
        min = l1[i]

print("max element in list= ",max)
print("min element in list= ",min)

