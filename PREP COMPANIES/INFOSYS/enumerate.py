# enumeration of list

my_list = [3,2,4]
print(my_list)

# [3, 2, 4]

for index,value in enumerate(my_list):
    print(index,value)

# 0 3
# 1 2
# 2 4


# using list comprehension

lc = [(index,value) for index,value in enumerate(my_list)]
print(lc)
# [(0, 3), (1, 2), (2, 4)]