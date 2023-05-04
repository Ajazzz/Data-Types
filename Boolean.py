
''' In Python, the Boolean data type is a built-in data type that can take on one of two possible values: True or False.
Boolean values are often used to represent the truth value of a condition or expression.'''

#Here are some examples of how to use Boolean data types in Python:

''' Checking if two values are equal: ''' 

a = 5
b = 10
c = a == b
print(c)  # Output: False

''' Checking if a number is greater than or equal to another number: '''

x = 8
y = 4
z = x >= y
print(z)  # Output: True

''' Checking if a string contains a certain character: '''

word = "hello"
contains_e = "e" in word
print(contains_e)  # Output: True


''' Combining multiple Boolean expressions using logical operators (and, or, not): '''

a = 5
b = 10
c = 15
result = (a < b) and (b < c) or not (a == c)
print(result)  # Output: True

# In this example, result is True because the expression (a < b) and (b < c) is true, and the expression not (a == c) is also true.
