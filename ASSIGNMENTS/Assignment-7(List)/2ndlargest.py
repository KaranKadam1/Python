# write a program to find second largest element in list

l1 = [1,2,3,4,5]
n = len(l1)

max = l1[0]
smax = 0

for i in range(1,n):
    if(max < l1[i]):
        smax = max
        max = l1[i]
    elif(smax < l1[i]):
        smax = l1[i]

print("list=",l1)
print("second largest element in list=",smax)

