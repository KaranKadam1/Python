'''
Q4)calculate the total cost of painting.the interior of bulding with four equal sized walls
'''
length = int(input("enter length = "))
width = int(input("enter width= "))

area = length*width
t_area = area*4


cost = int(input("enter cost= "))
total_cost = t_area*cost

print("total cost= ",total_cost)

