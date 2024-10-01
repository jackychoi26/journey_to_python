"""
** (double asterisks) will unpack key-value pairs of a dictionary and pass them as keyword arguments.
There're mainly 5 use cases for the dictionary unpacking:
1. Function Argument Passing
2. Merging Dictionaries
3. Dynamic Function Definitions
4. Object Initialization
5. String Formatting
"""

def greet(name="Guest", age=0):
    return f"Hello, {name}. You are {age} years old."

# Define a dictionary with key-value pairs
person = {'name': 'Alice', 'age': 30}

# Unpack the dictionary and pass the key-value pairs as keyword arguments
# Remember, the keys must match the parameter names
result = greet(**person)
print(result) # Hello, Alice. You are 30 years old.

"""
Merging dictionaries
"""
dict1 = {'x': 1, 'y': 2}
dict2 = {'y': 3, 'z': 4}

# Merge dict1 and dict2 using dictionary unpacking
merged_dict = {**dict1, **dict2}
print(merged_dict) # {'x': 1, 'y': 3, 'z': 4}

"""
Unpacking a dictionary for dynamic function call
"""

def dynamic_greeting(name='Guest', age=0, city='Unknown'):
    print(f"Hello, {name}!")
    print(f"You are {age} years old.")
    print(f"You're from {city}.")

# Define a dictionary with some arguments
person_data = {'name': 'Charlie', 'age': 25}

# Dynamically unpack the dictionary into the function
dynamic_greeting(**person_data)

# Combining Positional (*args) and Keyword Arguments (**kwargs)
def flexible_function(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")
    
# Call the function with both positional and keyword arguments
flexible_function(1, 2, 3, name='Alice', age=25, city='Paris')
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 25, 'city': 'Paris'}
