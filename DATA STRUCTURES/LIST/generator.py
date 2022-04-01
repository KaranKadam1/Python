# eg create a softi icecreame machine who knows how to make softi using algorithm
# machine has algorithm and using this it generates account numbers

import random

# Generator method -->contains yield keyword
def GetNumber(n):
    # No memory location
    # No return statement
    # Use yield keyword
    for i in range(n):
        yield random.randint(1,100000)  #give 1 no then paus ,again give 2 num then stops,not n times bc of yield key word

# the methods now generate a generator
result =GetNumber(10)
print(result) #it is generator object

print(next(result)) #output = 71760 -->one random num generated
# after 10 times print it will stop bc we mentioned limit in getnumber function
# not using memeory block just returning tr result

