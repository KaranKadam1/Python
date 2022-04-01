# read line by line

fp=""
try:
    fp = open("text.txt","r")

except FileNotFoundError:
    print("file does not exist")
else:
    for line in fp:
        print(line)
    fp.close()

