'''
 q4.We want to estimate the cost of painting a property. Interior wall painting cost  
is Rs.18 per sq.ft. and exterior wall painting cost is Rs.12 per sq.ft. 
Take input as
1. Number of Interior walls
2. Number of Exterior walls
3. Surface Area of each Interior Wall in units of square feet
4. Surface Area of each Exterior Wall in units of square feet'''


no_interior_walls = int(input("Enter no of interior walls= \n"))
no_exterior_walls = int(input("Enter no of exterior walls= \n"))

interior_total = 0
for i in range(no_interior_walls):
   surface_interior_wall = int(input("enter surface of interior wall="))
   interior_total += surface_interior_wall

exterior_total = 0
for i in range(no_exterior_walls):
   surface_exterior_wall = int(input("enter surface of exterior wall="))
   exterior_total += surface_exterior_wall

interior_cost = interior_total*10
exterior_cost = exterior_total*18

total_cost = interior_cost + exterior_cost

print("please pay= ",total_cost)
   