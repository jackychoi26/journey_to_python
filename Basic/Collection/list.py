# Python has a special syntax for accessing the last element in the list
list = ["trek", "cannondale", "redline"]
print(list[-1]) # >> redline

# By the same token, -2 will get the last 2 element
print(list[-2]) # >> cannondale

# Modifying a list
list[-1] = "Honda"
print(list[-1]) # >> Honda

# Appending element
list.append("Cat")
print(list[-1]) # >> Cat

# Inserting element
list.insert(0, "Dog")
print(list[0]) # >> Dog
print(list) # >> ['Dog', 'trek', 'cannondale', 'Honda', 'Cat']

# Removing item
del list[0]
print(list) # >> ['trek', 'cannondale', 'Honda', 'Cat']

# Popping item
item = list.pop()
print(item) # >> 'Cat'
print(list) # >> ['trek', 'cannondale', 'Honda']

# Popping second item
second_item = list.pop(1)
print(second_item) # >> cannondale
print(list) # >> ['trek', 'Honda]

# Removing item by value
list.remove('trek')
print(list) # >> ['Honda']

# Sorting a list in place
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # >> ['audi', 'bmw', 'subaru', 'toyota']

# Sorting a list immutably
new_cars = sorted(cars, reverse=True)
print(new_cars) # >> ['toyota', 'subaru', 'bmw', 'audi']
print(cars) # >> ['audi', 'bmw', 'subaru', 'toyota']

# Reverse a list
cars.reverse()
print(cars) # >> ['toyota', 'subaru', 'bmw', 'audi']

# Length of list
print(len(cars)) # >> 4