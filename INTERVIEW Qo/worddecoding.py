word = []

ch = "A"

for i in range(26):
    word.append(ch)
    ch = chr(ord(ch)+1)

print(word)

inputCode = input("input the word to be encoded=")
outputCode = ""

for i in range (len(inputCode)): #WORLD
    index_1 = word.index(inputCode[i])+1  #W 23
    
    x = i+3
    if(x > len(inputCode)-1):
        x = x - len(inputCode)
        index_3 = word.index(inputCode[x])+1 #L 12
    else:
        index_3 = word.index(inputCode[i+3])+1

    sum = index_1 + index_3  #35
    print(sum)

    if(sum>26):
        sum = sum-26  #9
    outputCode += word[sum-1]
print(outputCode)

