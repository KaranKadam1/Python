# compare two array is equal in size or not

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

count1 = 0
for x in arr1:
    count1 += 1

count2 = 0
for x in arr2:
    count2 += 1

if(count1 == count2):
    print("Equal in size")
else:
    print("Not Equal in size")