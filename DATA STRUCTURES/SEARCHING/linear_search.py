# linear search - searching algorithm

def linear_search(data,x):
    size = len(data)
    for i in range(0,size):
        if(x == data[i]):
            return i
    else:
        return -1


data = [40,10,5,70,80,35,71,50]
x = int(input("Enter the element you want to search= "))

index = linear_search(data,x)
if(index == -1):
    print("element is not present")
else:
    print("element is present at",index,"position")