# Python program to form new string where the first character and last character have been exchange

'''
inp = abcd
modified = dbca
'''

string = input("Enter a string=")

start = string[0]
end = string[-1]

new = end + string[1:-1]+start
print("Modified string=",new)