# remove duplicates from an array

array = [10,12,19,12,45,65,45]

new_arr = []

for x in array:
    if x not in new_arr:
        new_arr.append(x)

print(f"original array={array}")
print(f"after removing duplicates={new_arr}")