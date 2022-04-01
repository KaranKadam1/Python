'''
two geometric series in same series/two merged geometric series

given a series whose even term represents a geometric series with common ration 3
and the odd term is another series with common ratio 4

write a program to print the Nth number in the series .
here N is sent as a command-line argument,

exp;
1,1,3,4,9,16,27,....
'''

num = int(input())

if(num%2 == 0):
    N = 1*(4**int(num/2-1)) #even term
else:
    N = 1*(3**int(num/2)) #Odd term

print(N)

