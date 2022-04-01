# open method is used to reserve the channel
# if file not found

fp=""
try:
    # fp = open("abc.txt","r")
    fp = open("text.txt","r")

except FileNotFoundError:
    print("file does not exist")
else:
    # data = fp.read() #read all data from file
    data = fp.read(12)  #only five byts
    print(data)
    # print("file is present")
    fp.close()


