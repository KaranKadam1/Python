# sort list based on salary(3rd sublist element)

data=[[101,"seema",45000],[300,"Rajani",13000],[210,"Tannu",14000],[320,"suresh",35000]]

sort = sorted(data , key = lambda x : int(x[2]))
print(sort)

