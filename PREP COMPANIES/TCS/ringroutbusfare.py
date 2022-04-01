'''TCS - IMP
File Edit Format View Help A City Bus is a Ring Route Bus which runs in circular fashion.
That is, Bus once starts at the Source Bus Stop, halts at each Bus Stop in its Route and at
the end it reaches the Source Bus Stop again.

If there are n number of Stops and if the bus starts at Bus Stop 1,
then after nth Bus Stop, the next stop in the Route will be Bus Stop number 1 always. 
If there are n stops, there will be n paths.One path connects two stops. 
Distances (in meters) for all paths in Ring Route is given in array Path[] as given below:

Path [800, 600, 750, 900, 1400, 1200, 1100, 1500]

Fare is determined based on the distance covered from source to destination stop
as Distance between Input Source and Destination Stops can be measured by looking 
at values in array Path[] and fare can be calculated as per following criteria:

If d = 1000 metres, then fare = 5 INR

BusStops = ["TH","GA","IC","HA","TE","LU","NI","CA"]
(When calculating fare for others, the calculated fare containing any fraction value
should be ceiled. For example, for distance 900n when fare initially calculated is 4.5 
which must be ceiled to 5) 
Path is circular in function. Value at each index indicates distance
till current stop from the previous one. And each index position can be mapped withs
'''
import math

def getFare(source,destination):

    Path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
    BusStops = ["TH","GA","IC","HA","TE","LU","NI","CA"]

    start = BusStops.index(source)
    stop = BusStops.index(destination)

    distance = 0

    if(start < stop):
        for i in range(start,stop):
            distance += Path[i]

    else:
        while(start != stop):
            if(start == len(Path)):
                start = 0
            distance += Path[start]
            start += 1

    print("start=",start,"end=",stop)
    print("distance travel=",distance)
    fare = distance/1000*5
    print("total fare=",math.ceil(fare),"Rs")

source = input("enter source= ")
destination = input("enter destination= ")
getFare(source,destination)


'''
enter source= LU
enter destination= IC
start= 2 end= 2      
distance travel= 5200
total fare= 26 Rs
'''