# accept the number from user and check if this element is present in the list or not.
# also tell how manyt times it is present in the list.

l1 = [1,1,2,3,3,3,4,6]
num = int(input("Enter num to check="))
num_set = set(l1)

if num in l1:
    print(num,"is present in the list")
    for x in num_set:
        if num in num_set:
            n=l1.count(num)
        print(num,"is comming",n,"times")
        break    
       
else:
    print(num,"is not present is the list")