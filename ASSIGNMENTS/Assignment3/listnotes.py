
notes = [2000,500,200,100,50,20,10]

amount = int(input("enter the amount= "))

num_of_notes = 0

for i in notes:
    num_of_notes += amount//i
    amount = amount%i

print(f"number of notes are= {num_of_notes}")




notes = [2000,500,200,100,50,20,10]
amount = int(input("enter the amount= "))

num_of_notes = 0

for i in notes:
    temp = amount // i
    num_of_notes += temp
    amount = amount%i
    print(i,"notes = ",temp)
print("total no of notes= ",num_of_notes)
