'''
given a string str len N and a character char.the task is to check whether starting char and ending char is same.
if both are matching find the occurence of given char

if start and end char is matching then print ocuur of given char else print 0 if the input string len is less 
than 2,print-1

exp;
school-inp
o-char
0-op  start of char is s and end is l so both diff therefore 0

noon
o
2  both same so occur o=2
'''

str = input()
char = input()

if(len(str) < 2):
    print(-1)  #-1 is last element

elif(str[0] == str[-1]):  #if 1st element is matching last element
    print(str.count(char))

else:
    print(0)
