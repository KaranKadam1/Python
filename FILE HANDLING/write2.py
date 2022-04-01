fp = open("text.txt","w") 

# write to file
data =" "
while(data !="$"):
    data = input("enter data for file,press $ to stop= ") 
    if(data!="$"):
        fp.write(data)
        fp.write("\n")

fp.close()