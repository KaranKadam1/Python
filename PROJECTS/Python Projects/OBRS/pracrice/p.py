
def rotate(arr):
    return([arr[-1]] + arr[0:-1])
  


arr= list(map(int,input().split()))

x = rotate(arr)

for i in x:
    print(i,end=" ")

