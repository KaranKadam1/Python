# find frequency of data

data = [1,1,1,1,2,2,3,3,3,3,4,4,5,6]
result = set(data)

for x in result:
    print(x,data.count(x))



# find missing coins 
data = [1,1,1,1,2,2,3,3,3,3,4,4,5,6,6]
coins = set(data)
# 1,2,3,4,5,6

for x in coins:
    freq = data.count(x)
    if(freq%2 != 0):
        print(x,"is missing coin")
        break
