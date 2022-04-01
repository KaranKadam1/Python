X=int(input("enter X= "))
Y=int(input("enter Y= "))
Z=int(input("enter Z= "))

if(X > Y):
    if(X > Z):
        print(X,"is greatest")
    else:
        print(Z,"is greatest")

else:
    if(Y > Z):
        print(Y,"is greatest")
    else:
        print(Z,"is greatest")
