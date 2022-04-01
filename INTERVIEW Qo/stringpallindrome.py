# check whether the string is pallindrome or not
# string is immutable we cannot change it

string = input("enter a string=")

start = 0
end = len(string)-1

while(start < end):
    if(string[start] == string[end]):
        start += 1
        end -=1
    else:
        print(string,"is not pallindrome")
        break
else:
    print(string,"is pallindrome")
