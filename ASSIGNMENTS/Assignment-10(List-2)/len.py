# sort element in list according to the length of element within the list

list = ["karan", "amy", "sapna", "muhammad","kk"]

def sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if(len(list[j])>len(list[j+1])):
                list[j],list[j+1] = list[j+1],list[j]
    return list
print("original list=",list)
print("sorted according to length= ",sort(list))






# def Sorting(list):
	# list.sort(key=len)
	# return list
# print(Sorting(list))
