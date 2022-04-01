# write a program to reverse a list without using inbuilt functions

l1 = [1,2,3,4,5]
print("original list=",l1)

# using slicing
reverse_list = l1[::-1]
print(reverse_list)

# without slicing
start = 0
end = len(l1)-1

while(start<end):
    l1[start],l1[end] = l1[end],l1[start]
    start += 1
    end -= 1
print("reverse list=",l1)


