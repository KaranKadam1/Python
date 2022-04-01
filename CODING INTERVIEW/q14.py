# string palindrome

string = input()

if string[::-1]==string:
    print("Palindrome")
else:
    print("Not Palindrome")


# string reverse

string = input()

rev = ""
for i in range(len(string)):
    rev = string[i]+rev
print(rev)