# sum of all prime numbers between 1 to n

def sumofprime(num):

    sum = 0
    for n in range(2,num+1):
        for i in range(2,n):
            if(n%i == 0):
                break

        else:   
            print(n,"is prime")
            sum = sum+n
    print("sum of prime numbers=",sum)

num = int(input("Enter num= "))
sumofprime(num)



