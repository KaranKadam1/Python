# Remove the nth index character from a non-empty string

string = input("Enter string=")
n = int(input("enter the index of the character="))

first_half = string[:n]
second_half = string[n+1:]
New = first_half + second_half

print("Modified string=",New)

