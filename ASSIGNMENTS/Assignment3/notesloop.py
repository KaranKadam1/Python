amount = int(input("enter amount= "))

notes = [2000,1000,500,200,100,50,20,10]

notesCount = [0,0,0,0,0,0,0,0]

for i,j in zip(notes,notesCount):
    if amount>=i:
        j = amount//i
        amount = amount-j*i
        print(i," = ",j)