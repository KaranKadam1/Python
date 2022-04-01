data = "106,Suresh Jadhav,27000.0"
data = data.split(",")
print(data)

data[1]=input("enter new name=")
print(data)

data = ",".join(data)
print(data)