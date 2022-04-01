'''
Word is the key

One programming language has the following keywords that cannot be used as identifiers:
break, case, continue, default, defer, else, for, func, goto, if, map, range, return, struct, type, var

Write a program to find if the given word is a keyword or not

Input #1:
defer
Output:
defer is a keyword

Input #2:
While
Output:
While is not a keyword
'''

keywords = ["break","case","continue","default","defer","else","for","func","goto","if","map","range","return","struct","type","var"]

word = input()
if word in keywords:
    print(word+" is a keyword")
else:
    print(word+" is not a keyword")
