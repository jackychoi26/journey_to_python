# For loop
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)

for i in range(6):
    print(i) # 0, ...5

for j in range(2, 6):
    print(j) # 2, ...5
else:
    print("Finally finished!") # This is called after finishing the loop

for x in range(6):
    if x == 3: break # It ends at the 4th element
    print(x)
else:
    print("Finally finished!")

# With the continue statement we can stop the current iteration of the loop, 
# and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# While loop
i = 1
while i < 6:
    print(i)
    i += 1

# Same for while loop
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)