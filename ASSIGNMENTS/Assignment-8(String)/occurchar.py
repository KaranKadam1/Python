string =input()
char = input()

count = 0
for i in range(len(string)):
    if string[i] == char:
        count += 1

print(count)

'''
haveagoodday
a
3
'''