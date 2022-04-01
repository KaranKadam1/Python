#time complexity of bubble sort is o(n^2)

data = [5,4,3,2,1]
n = len(data)

for j in range(1,5):
    for i in range(n-j):
        if(data[i] > data[i+1]):
            data[i],data[i+1] = data[i+1],data[i]

print(data)