# reverse given number using recursion

def revint(n,r):
    if n == 0:
        return r
    else:
        return revint(n//10,r*10+n%10)
        
r =0
n = int(input("enter num="))
rev = revint(n,r)
print(rev)
