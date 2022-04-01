# find intersection of two list without using inbuilt function

A = [1,2,3,4,5]
B = [1,2,3,8,11]

result=[]
for x in A:
    if(x in B):
        result.append(x)
print("Intersection=",result)

