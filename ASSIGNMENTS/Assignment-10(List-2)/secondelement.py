# sort the list according to second element in sublist

list= [['karan', 10], ['akash', 5], ['ramesh', 20], ['nitesh', 15]]

sort = sorted(list , key = lambda x : int(x[1]))
print(sort)




# for j in range(1,n):
#     for i in range(n-j):
#         if(list[i] > list[i+1]):
#             list[i],list[i+1] = list[i+1],list[i]
# print("sorted list=",list)
