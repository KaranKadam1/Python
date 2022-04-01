
num = int(input("enter num of students= "))

for i in range(1,num+1):
    c = float(input("enter c marks= "))
    cp = float(input("enter cp marks= "))
    java = float(input("enter java marks= "))
    python = float(input("enter python marks= "))
    oop = float(input("enter oop marks= "))

    total = c + cp + java + python + oop
    average = total / 5
    percentage = (total/500)*100

print("total marks = ",total)
print("average marks= ",average)
print("percentage marks= ",percentage)
