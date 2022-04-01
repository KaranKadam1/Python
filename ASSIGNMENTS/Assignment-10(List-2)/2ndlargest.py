# Find second largest element in list using bubble sort

l = [11,2,45,6,99]
n = len(l)
# bubblesort

for j in range(1,5):
    for i in range(n-j):
        if(l[i] > l[i+1]):
            l[i],l[i+1] = l[i+1],l[i]

k = 2
print("Second largest element in list=",l[k+1])
