c=int(input("enter c marks= "))
cp=int(input("enter cp marks= "))
java=int(input("enter java marks= "))
python=int(input("enter python marks= "))
dbms=int(input("enter dbms marks= "))

result=(c+cp+java+python+dbms)/500*100

if(result>=90):
    print("Your grade is First class")
elif(result>=80):
    print("Your grade is Second class")
elif(result>=50):
    print("pass")
else:
    print("fail")


