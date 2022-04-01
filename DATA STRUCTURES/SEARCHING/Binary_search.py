
def binary_search(data,element):
    beg = 0
    end = len(data)-1

    while(beg <= end):
        mid = (beg+end)//2
        if(element == data[mid]):
            return mid
        elif(element < data[mid]):
            end = mid-1
        else:
            beg = mid+1
    else:
        return -1

data = [10,15,45,56,59,61,71,89,95]
element = int(input("Enter the element you want to search= "))
index = binary_search(data,element)

if(index == -1):
    print("element is not present")
else:
    print("element is present at",index,"position")