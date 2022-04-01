'''
Q2) write a program to accepts 3 digit number,if first digit is double of
second digit and half of third digit then display "yes,you have done it",
otherwise display "please try next time."
eg.- 428 ,214 etc
'''


num = int(input("enter 3 digit num= "))

c = num%10    #for last digit
num = num//10

b = num%10
num = num//10  #for 2nd digit

a = num%10    #for 1st digit

if(a==2*b and a==0.5*c):
    print("yes,you have done it")
else:
    print("please try next time")