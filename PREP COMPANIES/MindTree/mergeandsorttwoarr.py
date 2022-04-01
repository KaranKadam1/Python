# take two arrays then merge them and sort
'''
write a program to return a sorted array from two unsorted array.

exp;
10 5 15
20 3 2
2 3 5 10 15 20 - ouput
'''
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

final_array = arr1 + arr2  #merge two unsorted arrays

final_array.sort() #sort merged array

final_array_str = [str(x) for x in final_array] #each element in array 

print(" ".join(final_array_str)) #join all element in sorted order
