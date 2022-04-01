# find second highest number in integer array

# import array

# arr  = array.array('i',[])
# n = int(input())

# for i in range(1,n+1):
#     x = int(input())
#     arr.append(x)
# # print(arr)


arr = list(map(int,input().split()))
n = len(arr)

max = arr[0]
smax = 0

for i in range(1,n):
    if max<arr[i]:
        smax = max
        max = arr[i]
    elif smax<arr[i]:
        smax = arr[i]
print(f"Array={arr}")
print(f"Second Highest Number= {smax}")