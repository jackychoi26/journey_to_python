# Python's approach to handling large integers is somewhat similar to Java's 
# BigInteger class, but with a more seamless integration into the language's core

biggest_32bit_integer = 2_147_483_647
almost_infinite_size_integer = biggest_32bit_integer ** 99
print(almost_infinite_size_integer) ## >> Very very very large number!
