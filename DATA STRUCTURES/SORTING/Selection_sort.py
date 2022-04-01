#time complexity of selection sort is o(n^2)

data = [5,4,3,2,7,1]
n = len(data)

for i in range(0,n):
    min = data[i]
    index = i
    
    for j in range(i+1,n):
        if(min > data[j]):
            min = data[j]
            index = j

    data[i],data[index] = data[index],data[i]

print("Sorted data= ",data)