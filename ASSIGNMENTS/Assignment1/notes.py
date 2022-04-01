
# amount=int(input("enter amount= "))

# notes=[2000,500,200,100,50,20,10,5,1] #num of notes
# notesCheaker=[0,0,0,0,0,0,0,0,0]   #notesCounter

# print("currency count= ")

# for i,j in zip(notes,notesCheaker): #i for notes ,j for num of notes
#     if amount>=i:
#         j=amount//i
#         amount=amount-j*i
#         print(i," = ",j)


amount=int(input("enter amount= "))

no_of_notes=0

no_of_notes=amount//2000
amount=amount%2000

no_of_notes+=amount//500
amount=amount%500

no_of_notes+=amount//200
amount=amount%200

no_of_notes+=amount//100
amount=amount%100

no_of_notes+=amount//50
amount=amount%50

no_of_notes+=amount//20
amount=amount%20

no_of_notes+=amount//10
amount=amount%10

print("number of notes are= ",no_of_notes)


