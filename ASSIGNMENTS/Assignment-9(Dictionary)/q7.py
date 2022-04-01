# Remove the given key from a dictionary

dict = {1:5,2:4,3:3,4:2,5:1}
print("Original dictionary=",dict)

key = int(input("Enter key="))
if key in dict:
    del dict[key]
    print(key,"has been removed from dictionary")
    print("Updated Dictionary= ",dict)
else:
    print("Key not found!")


