# Precision: Python floats have a precision of about 15 to 17 decimal digits, 
# which corresponds to the 53 bits of precision of a double-precision 
# floating-point format (64 bits in total).

# Range: The range of Python floats is quite large due to the use of an exponent. 
# It can handle values from about 2.2e-308 to 1.8e+308. 
# Very small or very large numbers become subnormal or overflow to infinity, respectively.

# When you divide any 2 numbers, even if they are integers result
# in a whole number, it is still a float.
result = 4/2
print(result) # >> 2.0 

# When you mix an integer with a float in ANY operation, you'll get a float as well
result = 1 + 2.0
print(result) # >> 3.0

result = 2 * 3.0
print(result) # >> 6.0

# You can use underscores to divide number
universe_age = 14_000_000_000

# Multiple assignment
x, y, z = 0, 0, 0

# Constants
# Python does not come built-in with constants, but you can use all capital to indicate that
# you want this variable to be a constant that should not be modified throughout the
# program's life
MAX_CONNECTION = 5000

# Sometimes it goes wrong, but most of the time it is safe
print(0.2 + 0.1) # >> 0.30000000000000004
