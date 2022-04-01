# check if two strings are anagram  race=care  part=trap

string1 = input()
string2 = input()

if sorted(string1) == sorted(string2):
    print("Anagram")
else:
    print("Not Anagram")