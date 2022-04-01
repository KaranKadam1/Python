'''
Problem Statement

A doctor has a clinic where he serves his patients. The doctor’s consultation
fees are different for different groups of patients depending on their age.
If the patient’s age is below 17, fees is 200 INR. If the patient’s age is 
between 17 and 40, fees is 400 INR. If patient’s age is above 40, fees is 300 INR.
Write a code to calculate earnings in a day for which one array/List of values representing 
age of patients visited on that day is passed as input.

Note:

Age should not be zero or less than zero or above 120
Doctor consults a maximum of 20 patients a day
Enter age value (press Enter without a value to stop):
Example 1:

Input
20
30
40
50
2
3
14
 
Output
Total Income 2000 INR
'''
max_patient=20
age = []   #array/List of values representing age 
 
for i in range(max_patient): #Doctor consults a maximum of 20 patients a day
    
    n = input() #age of patients

    if(n == ""): #press Enter without a value to stop
        break
    elif int(n) in range(0,120): #less than zero or above 120
        age.append(int(n))
    else:  #Age should not be zero
        print("invalid input!")
        exit()

fees = 0

for x in age: #checks each patient age in list
    if x<17:  #age is below 17, fees is 200 INR.
        fees += 200
    elif(x<40): #age is below 40, fees is 400 INR.
        fees += 400
    else:       #If patient’s age is above 40, fees is 300 INR.
        fees += 300

print(f"Total Income {fees} INR")

