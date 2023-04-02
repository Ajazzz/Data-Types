# In Python, a float is a data type that represents decimal numbers. 
#It is a numeric type, just like integers, but with the ability to represent fractional values.
#Here's an example of defining a float variable in Python:

my_float = 3.14
print(my_float)
Output: 3.14

# You can perform arithmetic operations on floats just like you can with integers, 
#including addition, subtraction, multiplication, and division. Here are some examples:

x = 3.0
y = 2.0

print(x + y) # 5.0
print(x - y) # 1.0
print(x * y) # 6.0
print(x / y) # 1.5

# One thing to keep in mind when working with floats is that they are not always exact. 
#This is because the computer represents floats in binary, and not all decimal numbers can be represented exactly in binary. 
#As a result, you may encounter small rounding errors in calculations involving floats. For example:

print(0.1 + 0.2) # 0.30000000000000004

#To avoid issues with rounding errors, you can use the decimal module in Python, 
#which provides a way to perform exact decimal arithmetic. Here's an example:

from decimal import Decimal

x = Decimal('0.1')
y = Decimal('0.2')

print(x + y) # 0.3

##############

# Problem 1: Rounding error
print(0.1 + 0.2) # 0.30000000000000004

# Solution to Problem 1: Use round() function
print(round(0.1 + 0.2, 2)) # 0.3

# Problem 2: Division by zero
print(1.0/0.0) # Returns "inf"

# Solution to Problem 2: Use math module
import math
print(math.inf) # Prints "inf"

# Problem 3: Float comparison
a = 0.1 + 0.2
b = 0.3
print(a == b) # Returns "False"

# Solution to Problem 3: Use math.isclose() function
import math
print(math.isclose(a, b)) # Returns "True"

############

#In summary, floats are a data type in Python used to represent decimal numbers. 
#They can be used in arithmetic operations, but may have rounding errors due to the limitations of binary representation. 
#The decimal module can be used to perform exact decimal arithmetic.
