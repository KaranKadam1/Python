# convert distance given in feet and inches into meter and centimeters

feet= int(input("enter distance given in feet= "))
inch= int(input("enter distance given in inch= "))

meter= feet*0.3048
centimeter= inch*2.54
print("distance in meter=",meter,"m", "and centimeter=",centimeter,"c")