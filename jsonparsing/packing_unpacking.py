"""
In Python, packing refers to the process of putting values in a new tuple or list together.
Each value is separated by a comma.
"""

number1 = 1
number2 = 2
number3 = 3

# Tuple
tuple = (number1, number2, number3)

# List
list = [number1, number2, number3]

"""
* (asterisk) will pack the parameters into a tuple or list.
- * is used also for both power and multiplication. 
"""
def sumOf(*nums):
    print(f"Our numbers are {nums}")
    return sum(nums)

sumA = sumOf(number1, number2, number3) # Our numbers are (1, 2, 3)
print(sumA) # 6