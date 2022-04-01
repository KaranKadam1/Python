# program to find all chr occurence

from collections import Counter
import collections

word="aabacckkk"
w=Counter(word)
for i,n in w.items():
    print(f"{i} is comming {n} times")



# program to find which chr occurse more

word="abkk"
chars = []

for w in word:
    if w not in chars:
        chars.append(w)
    else:
        print(f"{w} is occuring more than once")



# remove occuring element

word="aaabkk"
char =" "

for w in word:
    if(w in char):
        pass
    else:
        char=char+w
print("after removing duplicate item:",char)


