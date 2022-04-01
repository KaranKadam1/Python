# Count number of vowels in string

string = input("Enter a string=")
vowels = 0

for x in string:
    if(x in "aeiou"):
        vowels = vowels+1
print(vowels)