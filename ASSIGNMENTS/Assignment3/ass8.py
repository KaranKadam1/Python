'''
a.	1! +  2! + 3! + 4! + …..n! 
1+2+3+4...+n =>sum =sum+i!
'''

sum = 0

n = int(input("Enter a number= "))

for i in range(1,n+1):
    #Factorial
    f = 1
    for j in range(1,i+1):
        f =f*j
    sum = sum + f
    print("Sum = ",sum)

print("Facorial = ",f)