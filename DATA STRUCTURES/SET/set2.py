A={1,2,3,4,5}
B={4,5,6,7}

# Union 
c = A.union(B)
print(c)
c = A|B
print("union=",c)


# intersection
c = A.intersection(B)
print(c)
c = A & B
print(c)

# Difference
c = A.difference(B)
print(c)
c = A-B
print(c)

# Symmetric difference
c = A.symmetric_difference(B)
print(c)
c = A^B
print(c)