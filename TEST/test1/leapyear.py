'''
Q1)check if input year is leap year or not
'''

year = int(input("enter year= "))

if(year%4 == 0 or year%400 ==0 and year%100 != 0):
    print(year,"is leap year")
else:
    print(year,"is not leap year")




year = int(input("enter year= "))

if(year%4==0):
    if(year%100 == 0):
        if(year%400 == 0):
            print("leap")
        else:
            print("not leap")
    else:
        print("leap")
else:
    print("not leap")
