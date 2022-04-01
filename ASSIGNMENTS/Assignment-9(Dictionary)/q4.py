# Generate a dictionary that contains numbers(between 1 and n) in the form(x,x*x)

n = int(input("Enter n="))

dict = {x:x*x for x in range(1,n+1)}
print(dict)