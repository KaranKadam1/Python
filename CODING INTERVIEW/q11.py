# check if the number is binary

def check(num):
    p = set(num)
    s = {'0','1'}

    if p==s or p=={'0'} or p=={'1'}:
        print("Binary")
    else:
        print("Not Binary")
num = input()
check(num)





