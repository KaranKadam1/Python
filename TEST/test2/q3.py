# 3.	Write a program to accept basic salary of n emp. (n should be accepted from user).
#  If basic salary is below 20000 then da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and hra=20%. 
# Based on this calculate the total salary of each emp and also total salary of all emp.


n = int(input("enter num of employees="))
total_sal = 0 

for i in range(n):
    basic_salary = float(input("enter salary= "))
    
    if(basic_salary<20000):
        da = basic_salary *(10/100)
        hra = basic_salary*(15/100)
        ta = basic_salary*(12/100)
       
    else:
        da = basic_salary*(15/100)
        hra = basic_salary*(20/100)
        ta = basic_salary*(18/100)

    total = basic_salary + da +hra +ta
    total_sal += total
    print("salary of employee= ",total,"Rs")

print("total salay of all employee= ",total_sal,"Rs")

