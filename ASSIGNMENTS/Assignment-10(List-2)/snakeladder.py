# print 1 to 100 in snake ladder pattern

for i in range(10,0,-1):
    x = i*10
    
    data = []
    for j in range(0,10):
        data.append(x-j)
    if(i%2 != 0):
        data.reverse()
    
    for x in data:
        print(x,end=" ")
    print()