# A tuple looks just like a list, except you use parentheses instead of square
# brackets. Once you define a tuple, you can access individual elements by
# using each item’s index, just as you would for a list.

dimensions = (200, 50)
print(dimensions[0]) # >> 200
print(dimensions[1]) # >> 50

# This will not work as Tuple cannot be reassigned
# dimensions[0] = 250

# Sometimes Tuple can be 1 element
# Usually doesn't make sense, but it could be the case for the generated one
my_tuple = (3,)

for dimension in dimensions:
    print(dimension) # >> 200 >> 50

# However, you can overwrite a Tuple pointer
dimensions = (250, 49)
print(dimensions) # >> (250, 49)