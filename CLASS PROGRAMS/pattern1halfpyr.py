n=int(input("enter num= "))

for i in range(1,n):
    for j in range(1,i+1):
        print("*",end =" ")
    print()   #work as \n for new line

'''
enter num= 5
* 
* *
* * *
* * * *
'''