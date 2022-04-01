# write a program to create a new list from existing list which contains cube of each number of list

l1 = [1,2,3,4,5]

new_list=[]

for x in l1:
    new_list.append(x**3)
print("old list= ",l1)
print("new list= ",new_list)