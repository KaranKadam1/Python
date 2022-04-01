# r+ = read + write, error if file not exist
# w+ = write + read
# a+ = append + read
# rb = read binary
# tell = to tell where are we(from start to end moving pointer in byts)
# seak = to position/move the file pointer(beg=0,current=1,end=2,x(how much we have to move)=offset)->seak(offset,pos)

with open("data.txt","r") as fp:
    print(fp.tell())
    fp.read(10)
    print(fp.tell())
    fp.read()   #pointer at end
    print(fp.tell())


with open("data.txt","rb") as fp:
    print(fp.tell())
    fp.seek(10,0) #(offset,pos) move 10 byts forward from beg
    print(fp.tell())
    fp.seek(0,2) #move to end
    print(fp.tell())
    fp.seek(-10,2) #back
    print(fp.tell())


fp = open("data.txt","r+")
print(fp.tell())
fp.seek(0,2)
fp.write("\nNew Line") #add/overrite existing data
fp.close()


fp = open("data.txt","w+")
print(fp.tell())
fp.seek(0,2)
fp.write("First Line\n") 
fp.write("Second Line\n") 
fp.write("Third Line\n") 
fp.seek(0,0)#beg
print(fp.read())
fp.close()


#Check if the file is present or not-->
from os import path
import os
if(path.exists("data.txt")):
    print("yes the file is present")
else:
    print("no the file is not present")


#Rename the file
os.rename("data.txt","newfile.txt")


# delete the file
os.remove("text.txt")