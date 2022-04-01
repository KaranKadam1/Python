# merge two list and sort without using inbuilt function

l1 = [5,12,66,4,99]
l2 = [65,23,48,3]

final_list = l1 + l2
n =len(final_list)

for j in range(1,n):
    for i in range(n-j):
        if(final_list[i] > final_list[i+1]):
            final_list[i],final_list[i+1] = final_list[i+1],final_list[i]

print("sorted list=",final_list)

