# it will not del recent content like write

fp = open("abc.txt","a") #if file not found then it will create one 

fp.write("fourth\n")
fp.write("fifth\n")
fp.write("six\n")

fp.close()



