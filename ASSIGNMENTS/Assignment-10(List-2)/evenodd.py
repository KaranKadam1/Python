# Put even and odd elements of a list into different list

list = [2,51,1,8,9,11,86,99]

even = []
odd = []

for x in list:
    if (x%2 == 0):
        even.append(x)
    else:
        odd.append(x)
print("even list=",even)
print("odd list=",odd)


